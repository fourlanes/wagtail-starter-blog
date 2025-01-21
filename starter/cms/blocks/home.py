from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    ListBlock,
    PageChooserBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField

from starter.cms.blocks.common import ButtonBlock, CaptionedImage, ContactUsBlock, HeadingBlock, RichText


class OurStack(StructBlock):
    class Meta:
        help_text = "A static view of our tech stack, with a dynamic heading and content"
        icon = "bars"
        label = "Our Stack"
        template = "blocks/our_stack.html"

    heading = CharBlock(required=True)
    content = TextBlock(required=True)
    button = ButtonBlock(required=False)


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """

    text = TextBlock()
    source = TextBlock(required=False, help_text="Who is this quote acredited to?")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"


class HeroBlock(StructBlock):
    image = ImageChooserBlock()
    overlay = ChoiceBlock(
        choices=[
            ("basic", "Basic"),
            ("theme-coloured", "Theme Coloured"),
            ("theme-gradient", "Theme Coloured Gradient"),
            ("none", "None"),
        ],
        default="theme-coloured",
    )
    content = ListBlock(HeadingBlock(template="cms/blocks/heading_block.html"))
    links = ListBlock(
        StructBlock([("caption", CharBlock(required=False)), ("page", PageChooserBlock(required=True))]),
        required=False,
    )
    button = ButtonBlock(required=False, template="cms/blocks/hero_block_button.html")

    class Meta:
        template = "cms/blocks/hero_block.html"
        icon = "image"


class HomeContentStreamBlock(StreamBlock):
    hero = HeroBlock()
    contact_us = ContactUsBlock()
    richtext = RichText(template="cms/blocks/rich_text.html")
    captioned_image = CaptionedImage(template="cms/blocks/captioned_image.html")
    our_stack = OurStack()

    required = True


def content_streamfield(blank=False, null=True):
    return StreamField(
        [("rich_text", RichText()), ("captioned_image", CaptionedImage()), ("blockquote", BlockQuote())],
        blank=blank,
        null=null,
        use_json_field=True,
    )
