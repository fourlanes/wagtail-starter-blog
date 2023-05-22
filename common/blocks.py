from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    EmailBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.images.blocks import ImageChooserBlock

from common.constants import STREAMFIELD_RICHTEXT_FEATURES


class HeadingBlock(StructBlock):
    heading = ChoiceBlock(
        default="h1",
        choices=(
            ("h1", "Heading 1"),
            ("h2", "Heading 2"),
            ("h3", "Heading 3"),
            ("h4", "Heading 4"),
        ),
    )
    text = StreamBlock(
        [
            (
                "simple_text",
                StructBlock([("text", TextBlock(required=False, label="Text"))], icon="title", label="Simple Text"),
            ),
            (
                "styled_text",
                StructBlock([("text", TextBlock(required=False, label="Text"))], icon="title", label="Styled Text"),
            ),
        ],
    )

    class Meta:
        template = "blocks/heading_block.html"
        icon = "title"


class HeroContent(StreamBlock):
    heading = HeadingBlock()

    required = False


class HeroBlock(StructBlock):
    image = ImageChooserBlock(required=False)
    content = ListBlock(HeadingBlock())

    class Meta:
        template = "blocks/hero_block.html"
        icon = "image"


class ContactUsBlock(StructBlock):
    heading = TextBlock()
    sub_heading = TextBlock(label="Sub-Heading")
    photo = ImageChooserBlock(required=False)
    email = EmailBlock()
    phone_number = CharBlock(max_length=20, label="Phone Number")

    class Meta:
        template = "blocks/contact_us_block.html"
        icon = "mail"
        label = "Contact Us"


class AnchorBlock(StructBlock):
    anchor_id = CharBlock(required=True, help_text="The unique indentifier for this anchor")
    name = CharBlock(required=False, help_text="Used on the navigation link (if used)")

    class Meta:
        icon = "thumbtack"
        template = "blocks/anchor_block.html"


class RichText(StructBlock):
    class Meta:
        template = "blocks/rich_text.html"

    rich_text = RichTextBlock(features=STREAMFIELD_RICHTEXT_FEATURES)
