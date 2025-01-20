from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from starter.cms.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from starter.cms.utils import ContactUsFooterPanels
from starter.cms.blocks import HomeContentStreamBlock


class HomePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    parent_page_types = []

    content = StreamField(HomeContentStreamBlock(), use_json_field=True, null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        ContactUsFooterPanels(),
    ]

    class Meta:
        verbose_name = "Home Page"
