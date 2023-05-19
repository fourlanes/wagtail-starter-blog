from wagtail.blocks import RichTextBlock, StructBlock
from wagtail.fields import StreamField

from common.constants import STREAMFIELD_RICHTEXT_FEATURES


class RichText(StructBlock):
    class Meta:
        template = "blocks/rich_text.html"

    rich_text = RichTextBlock()


def content_streamfield(blank=False, null=True):
    return StreamField(
        [
            ("rich_text", RichText(features=STREAMFIELD_RICHTEXT_FEATURES)),
        ],
        blank=blank,
        null=null,
        use_json_field=True,
    )
