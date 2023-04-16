from wagtail.blocks import ListBlock, StreamBlock

from common.blocks import ContactUsBlock, HeroBlock as CommonHeroBlock, HeadingBlock


class HeroBlock(CommonHeroBlock):
    content = ListBlock(HeadingBlock(template="home/blocks/heading_block.html"))


class HomeContentStreamBlock(StreamBlock):
    hero = HeroBlock(template="home/blocks/hero_block.html")
    contact_us = ContactUsBlock()

    required = True
