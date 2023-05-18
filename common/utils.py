from django.db import models

from wagtail.admin.panels import FieldPanel


def ForeignKeyField(
    model=None, required=False, on_delete=models.SET_NULL, related_name="+", **kwargs
) -> models.ForeignKey:
    if not model:
        raise ValueError("ForeignKeyField requires a valid model string reference")
    required = not required
    return models.ForeignKey(
        model, null=True, blank=required, on_delete=on_delete, related_name=related_name, **kwargs
    )


def WagtailImageField(required=False, **kwargs) -> models.ForeignKey:
    return ForeignKeyField(model="wagtailimages.Image", required=required, **kwargs)


def ContactUsFooterPanels():
    return FieldPanel("show_contact_us_footer")
