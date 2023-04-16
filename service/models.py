from django.db import models  # noqa: F401

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels
from common.blocks import ContactUsBlock, HeroBlock


class ServicePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Services Page"

    parent_page_type = ["home.HomePage"]
    subpage_type = ["service.ServicePage"]

    content = StreamField(
        [("hero", HeroBlock()), ("contact_us", ContactUsBlock())], use_json_field=True, null=True, blank=False
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        ContactUsFooterPanels(),
    ]
