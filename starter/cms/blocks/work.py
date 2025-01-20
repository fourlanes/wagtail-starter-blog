from wagtail.blocks import (
    CharBlock,
    ListBlock,
    PageChooserBlock,
    StructBlock,
    TextBlock,
)


class WorkBlock(StructBlock):
    class Meta:
        icon = "radio-full"
        template = "cms/blocks/work-block.html"
        form_classname = "label-capitalise"

    heading = TextBlock(required=True, default="Our Work")
    work_articles = ListBlock(PageChooserBlock(page_type="cms.WorkArticle"))
    work_topic = CharBlock(
        required=False, help_text="The tag/topic for filtering the content on the work page e.g. wagtail"
    )
    show_more_caption = CharBlock(max_length=100, default="See more work", required=False)
