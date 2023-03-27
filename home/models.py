from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from home.blocks import HomeContentStreamBlock


class HomePage(Page):
    parent_page_types = []

    content = StreamField(HomeContentStreamBlock(), use_json_field=True, null=True, blank=False)

    content_panels = Page.content_panels + [
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Home Page"
