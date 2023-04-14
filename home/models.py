from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels
from home.blocks import HomeContentStreamBlock


class HomePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    parent_page_types = []

    content = StreamField(HomeContentStreamBlock(), use_json_field=True, null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        ContactUsFooterPanels(),
    ]

    class Meta:
        verbose_name = "Home Page"
