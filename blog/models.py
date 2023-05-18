from django.db import models  # noqa: F401

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels, WagtailImageField


class Topic(TaggedItemBase):
    content_object = ParentalKey(Page, on_delete=models.CASCADE, related_name="page_topics")


class BlogListing(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Blog Listing"

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.ArticlePage"]

    content_panels = Page.content_panels + [
        ContactUsFooterPanels(),
    ]


class ArticlePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Article Page"

    parent_page_types = ["blog.BlogListing", "work.WorkListing"]

    hero_image = WagtailImageField(verbose_name="Hero Image")
    topics = ClusterTaggableManager(through=Topic, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_image"),
        FieldPanel("topics"),
        ContactUsFooterPanels(),
    ]
