from django.db import models

from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel

from common.utils import WagtailImageField


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
