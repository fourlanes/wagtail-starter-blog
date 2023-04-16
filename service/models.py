from django.db import models  # noqa: F401

from wagtail.models import Page

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels


class ServicePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Services Page"

    parent_page_type = ["home.HomePage"]
    subpage_type = ["service.ServicePage"]

    content_panels = Page.content_panels + [
        ContactUsFooterPanels(),
    ]
