from django.db import models  # noqa: F401

from wagtail.models import Page

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels


class WorkListing(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Work Listing"

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.ArticlePage"]
    max_count = 1

    content_panels = Page.content_panels + [
        ContactUsFooterPanels(),
    ]
