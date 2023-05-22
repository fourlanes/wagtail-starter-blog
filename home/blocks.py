from wagtail.blocks import ListBlock, StreamBlock, StructBlock
from wagtail.images.blocks import ImageChooserBlock

from common.blocks import ContactUsBlock, HeadingBlock, RichText


class HeroBlock(StructBlock):
    image = ImageChooserBlock()
    content = ListBlock(HeadingBlock(template="home/blocks/heading_block.html"))

    class Meta:
        template = "home/blocks/hero_block.html"
        icon = "image"


class HomeContentStreamBlock(StreamBlock):
    hero = HeroBlock()
    contact_us = ContactUsBlock()
    richtext = RichText(template="home/blocks/rich_text.html")

    required = True
