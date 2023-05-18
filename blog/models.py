import datetime

from django.db import models  # noqa: F401

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TagBase, TaggedItemBase

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels, ForeignKeyField, WagtailImageField


@register_snippet
class ArticleTopic(TagBase):
    free_tagging = False

    panels = [
        FieldPanel("name"),
    ]

    class Meta:
        verbose_name = "Article Topic"
        verbose_name_plural = "Article Topics"


class Topic(TaggedItemBase):
    tag = models.ForeignKey(ArticleTopic, related_name="tagged_article", on_delete=models.CASCADE)
    content_object = ParentalKey(Page, on_delete=models.CASCADE, related_name="page_topics")


class BlogListing(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Blog Listing"

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.ArticlePage"]
    max_count = 1

    content_panels = Page.content_panels + [
        ContactUsFooterPanels(),
    ]


class ArticlePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Article Page"

    parent_page_types = ["blog.BlogListing", "work.WorkListing"]

    hero_image = WagtailImageField(verbose_name="Hero Image")
    topics = ClusterTaggableManager(through=Topic, blank=True)
    author = ForeignKeyField(model="team.Author")
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="This date will be used for display and ordering",
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_image"),
        FieldPanel("topics"),
        FieldPanel("author"),
        FieldPanel("published_date"),
        ContactUsFooterPanels(),
    ]

    def save(self, *args, **kwargs):
        if not self.published_date:
            self.published_date = datetime.datetime.now()
        super().save(*args, **kwargs)
