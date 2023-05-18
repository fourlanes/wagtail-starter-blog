from wagtail.blocks import CharBlock, ListBlock, RichTextBlock, StructBlock, TextBlock

from common.constants import SIMPLE_RICHTEXT_FEATURES


class ServicesBlock(StructBlock):
    class Meta:
        icon = "radio-full"
        template = "service/blocks/services_block.html"

    heading = TextBlock(required=True, default="Services")
    services = ListBlock(
        StructBlock(
            [("heading", CharBlock(required=True)), ("description", RichTextBlock(features=SIMPLE_RICHTEXT_FEATURES))]
        )
    )
