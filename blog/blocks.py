from wagtail.blocks import RichTextBlock, StructBlock
from wagtail.fields import StreamField

from common.constants import STREAMFIELD_RICHTEXT_FEATURES


class RichText(StructBlock):
    class Meta:
        template = "blocks/rich_text.html"

    rich_text = RichTextBlock(features=STREAMFIELD_RICHTEXT_FEATURES)


def content_streamfield(blank=False, null=True):
    return StreamField(
        [
            ("rich_text", RichText()),
        ],
        blank=blank,
        null=null,
        use_json_field=True,
    )
