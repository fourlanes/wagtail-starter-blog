from django.db import models
from django.utils.translation import gettext_lazy

from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.admin.widgets.slug import SlugInput


class CustomMetadataPageMixin(MetadataPageMixin):
    class Meta:
        abstract = True

    promote_panels = [
        MultiFieldPanel(
            [
                FieldPanel("slug", widget=SlugInput),
                FieldPanel("seo_title"),
                FieldPanel("search_description"),
                FieldPanel("search_image"),
            ],
            gettext_lazy("For Search Engines"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("show_in_menus"),
            ],
            gettext_lazy("For Site Menus"),
        ),
    ]

    def get_meta_image(self):
        if getattr(self.specific, "search_image", None):
            return self.specific.search_image
        elif getattr(self.specific, "hero_image", None):
            return self.specific.hero_image
        return super(CustomMetadataPageMixin, self).get_meta_image()

    def get_meta_description(self):
        return self.search_description if self.search_description else self.seo_title or self.title

    def get_meta_title(self):
        site = self.get_site
        site_name = site.site_name if hasattr(site, "site_name") else "Line 23"
        return "%s - %s" % (self.seo_title if self.seo_title else self.title, site_name)


class ContactUsFooterMixin(models.Model):
    class Meta:
        abstract = True

    show_contact_us_footer = models.BooleanField(
        default=True,
        verbose_name="Show Contact Us Footer",
        help_text="Useful when u want to use the Contact Us Block for a custom contact",
    )
