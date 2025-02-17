from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock

from starter.cms.constants import SIMPLE_RICHTEXT_FEATURES


class ClientsBlock(StructBlock):
    class Meta:
        icon = "radio-empty"
        template = "cms/blocks/clients_block.html"

    heading = TextBlock(required=True, default="Clients")
    clients = ListBlock(StructBlock([("website", URLBlock(required=False)), ("logo", ImageChooserBlock())]))


class ServicesBlock(StructBlock):
    class Meta:
        icon = "radio-full"
        template = "cms/blocks/services_block.html"

    heading = TextBlock(required=True, default="Services")
    services = ListBlock(
        StructBlock(
            [
                ("heading", CharBlock(required=True)),
                ("description", RichTextBlock(features=SIMPLE_RICHTEXT_FEATURES)),
                ("page", PageChooserBlock(required=False)),
            ]
        )
    )
