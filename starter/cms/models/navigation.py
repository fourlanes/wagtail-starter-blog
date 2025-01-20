from django.db import models

from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from starter.cms.utils import ForeignKeyField, WagtailImageField


@register_setting
class ContactUsFooter(BaseGenericSetting):
    heading = models.TextField()
    sub_heading = models.TextField(verbose_name="Sub-Heading")
    photo = WagtailImageField(required=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, verbose_name="Phone Number")
    address = models.TextField(null=True, blank=True)

    panels = [
        FieldPanel("heading"),
        FieldPanel("sub_heading"),
        FieldPanel("photo"),
        FieldPanel("email"),
        FieldPanel("phone_number"),
        FieldPanel("address"),
    ]

    class Meta:
        verbose_name = "Contact Us Footer"


@register_setting
class NavCTA(BaseGenericSetting):
    class Meta:
        verbose_name = "Nav Call to Action"

    caption = models.CharField(null=False, blank=False)
    page = ForeignKeyField(
        model=Page,
        help_text="For the link/button to show, either this or the url are required",
    )
    url = models.URLField(blank=True, null=True, help_text="An alternative to an internal page")

    panels = [FieldPanel("caption"), FieldPanel("page"), FieldPanel("url")]
