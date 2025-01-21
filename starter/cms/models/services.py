from django.utils.functional import cached_property

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock

from starter.cms.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from starter.cms.utils import ContactUsFooterPanels
from starter.cms.blocks import AnchorBlock, ContactUsBlock, HeroBlock
from starter.cms.blocks import ClientsBlock, ServicesBlock
from starter.cms.blocks import WorkBlock


class ServicePage(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Services Page"

    parent_page_type = ["cms.HomePage"]
    subpage_type = ["cms.ServicePage"]

    content = StreamField(
        [
            ("hero", HeroBlock()),
            ("contact_us", ContactUsBlock()),
            ("richtext", RichTextBlock(template="service/blocks/richtext.html")),
            ("anchor", AnchorBlock()),
            ("services", ServicesBlock()),
            ("clients", ClientsBlock()),
            ("work", WorkBlock()),
        ],
        use_json_field=True,
        null=True,
        blank=False,
    )

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        ContactUsFooterPanels(),
    ]

    @cached_property
    def sections(self):
        sections = []
        for block in self.content:
            if block.block_type == "anchor":
                sections.append(block)
        return sections
