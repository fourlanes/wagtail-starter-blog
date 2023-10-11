from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    EmailBlock,
    ListBlock,
    PageChooserBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock

from common.constants import STREAMFIELD_RICHTEXT_FEATURES


class AbstractLinkBlock(StructBlock):
    caption = CharBlock(required=False, help_text="Leave blank if you wish to use the page title as a caption")
    page = PageChooserBlock(
        required=False, help_text="For the link/button to show, either this or the url are required"
    )
    url = URLBlock(required=False, help_text="An alternative to an internal page")

    class Meta:
        icon = "link"
        abstract = True


class LinkBlock(AbstractLinkBlock):
    class Meta:
        icon = "link"
        template = "blocks/link_block.html"


class ButtonBlock(AbstractLinkBlock):
    style = ChoiceBlock([("primary", "Primary"), ("secondary", "Secondary")], required=False, default="primary")

    class Meta:
        template = "blocks/button_block.html"
        label = "A Link Button"
        form_classname = "button-block indent-fields"
        help_text = "Displays a link/button that navigates to the specified page or url when clicked"


class ImageLink(AbstractLinkBlock):
    class Meta:
        icon = "link"
        template = "blocks/image_link.html"

    image = ImageChooserBlock()


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


class OurStack(StructBlock):
    class Meta:
        help_text = "A static view of our tech stack, with a dynamic heading and content"
        icon = "bars"
        label = "Our Stack"
        template = "blocks/our_stack.html"

    heading = CharBlock(required=True)
    content = TextBlock(required=True)
    button = ButtonBlock(required=False)
