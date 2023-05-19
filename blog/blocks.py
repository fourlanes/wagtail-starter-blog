from wagtail.blocks import CharBlock, RichTextBlock, StructBlock, TextBlock, URLBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from common.constants import STREAMFIELD_RICHTEXT_FEATURES


class RichText(StructBlock):
    class Meta:
        template = "blocks/rich_text.html"

    rich_text = RichTextBlock(features=STREAMFIELD_RICHTEXT_FEATURES)


class CaptionedImage(StructBlock):
    class Meta:
        help_text = "Displays an image with an optionally linked caption."
        icon = "image"
        label = "Captioned image"
        template = "blocks/captioned_image.html"

    image = ImageChooserBlock(help_text="Optimal minimum width 800px")
    caption = TextBlock(required=False, help_text="Optional: caption text to appear below the image")
    caption_link = URLBlock(required=False, help_text="Optional: external link to appear below the image")
    caption_label = CharBlock(
        required=False, help_text="Optional: label for the caption link, defaults to the link if left blank"
    )


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows render text in a blockquote element
    """

    text = TextBlock()
    source = TextBlock(required=False, help_text="Who is this quote acredited to?")

    class Meta:
        icon = "openquote"
        template = "blocks/blockquote.html"


def content_streamfield(blank=False, null=True):
    return StreamField(
        [("rich_text", RichText()), ("captioned_image", CaptionedImage()), ("blockquote", BlockQuote())],
        blank=blank,
        null=null,
        use_json_field=True,
    )
