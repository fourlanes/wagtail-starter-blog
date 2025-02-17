import datetime

from django.db import models
from django.contrib.contenttypes.models import ContentType

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TagBase, TaggedItemBase

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from starter.cms.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from starter.cms.utils import ContactUsFooterPanels, ForeignKeyField, WagtailImageField
from starter.cms.blocks import content_streamfield


class ArticleTopic(TagBase):
    free_tagging = False

    class Meta:
        verbose_name = "Article Topic"
        verbose_name_plural = "Article Topics"


class Topic(TaggedItemBase):
    tag = models.ForeignKey(ArticleTopic, related_name="tagged_article", on_delete=models.CASCADE)
    content_object = ParentalKey("cms.ArticlePage", on_delete=models.CASCADE, related_name="page_topics")


class BlogListing(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Blog Listing"

    parent_page_types = ["cms.HomePage"]
    subpage_types = ["cms.ArticlePage"]
    max_count = 1

    content_panels = Page.content_panels + [
        ContactUsFooterPanels(),
    ]

    def get_context(self, request):
        context = super(BlogListing, self).get_context(request)

        article_content_type = ContentType.objects.get_for_model(ArticlePage)
        context["topics"] = (
            ArticleTopic.objects.filter(tagged_article__content_object__content_type=article_content_type)
            .distinct()
            .order_by("name")
        )

        return context


class ArticlePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Blog Article"

    parent_page_types = ["cms.BlogListing"]

    hero_image = WagtailImageField(verbose_name="Hero Image")
    topics = ClusterTaggableManager(through=Topic, blank=True)
    author = ForeignKeyField(model="cms.Author")
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="This date will be used for display and ordering",
    )
    content = content_streamfield()

    content_panels = Page.content_panels + [
        FieldPanel("hero_image"),
        FieldPanel("topics"),
        FieldPanel("author"),
        FieldPanel("published_date"),
        FieldPanel("content"),
        ContactUsFooterPanels(),
    ]

    def save(self, *args, **kwargs):
        if not self.published_date:
            self.published_date = datetime.datetime.now()
        super().save(*args, **kwargs)

    def get_context(self, request):
        context = super(ArticlePage, self).get_context(request)

        context["topics"] = [topic for topic in self.topics.all()]

        return context
