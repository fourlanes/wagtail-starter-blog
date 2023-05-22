from wagtail.blocks import StructBlock, TextBlock
from wagtail.fields import StreamField

from common.blocks import CaptionedImage, RichText


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
