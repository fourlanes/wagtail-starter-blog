from wagtail.blocks import ChoiceBlock, StreamBlock, StructBlock, TextBlock, EmailBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


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
    text = TextBlock()

    class Meta:
        template = "home/blocks/heading_block.html"
        icon = "title"


class HeroContent(StreamBlock):
    heading = HeadingBlock()

    required = False


class HeroBlock(StructBlock):
    image = ImageChooserBlock()
    content = HeroContent()

    class Meta:
        template = "home/blocks/hero_block.html"
        icon = "image"


class ContactUsBlock(StructBlock):
    heading = TextBlock()
    sub_heading = TextBlock(label="Sub-Heading")
    photo = ImageChooserBlock(required=False)
    email = EmailBlock()
    phone_number = CharBlock(max_length=20, label="Phone Number")

    class Meta:
        template = "home/blocks/contact_us_block.html"
        icon = "mail"
        label = "Contact Us"


class HomeContentStreamBlock(StreamBlock):
    hero = HeroBlock()
    contact_us = ContactUsBlock()

    required = True
