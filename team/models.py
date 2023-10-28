from django.db import models

from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search import index

from common.utils import WagtailImageField


AUTHOR_CHOICES = (
    ("author_name", "Author name"),
    ("person_page", "Person page"),
)


@register_snippet
class Author(index.Indexed, models.Model):  # FIXME: use more generic Person class
    class Meta:
        verbose_name = "Author"
        ordering = ["author_name"]

    author_type = models.CharField(
        max_length=15,
        choices=AUTHOR_CHOICES,
        default=AUTHOR_CHOICES[0][0],
    )
    author_photo = WagtailImageField()
    author_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Add an author name (e.g. [first name last name])",
    )
    author_credential = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional: Add an author credential to display alongside the author name (e.g [role, organisation])",
    )

    search_fields = [
        index.AutocompleteField("author_name"),
    ]

    panels = [
        FieldPanel("author_type"),
        FieldPanel("author_photo"),
        MultiFieldPanel(
            [
                FieldPanel("author_name"),
                FieldPanel("author_credential"),
            ],
            heading="Author and Credential",
            help_text="Add an author name and their credentials.",
        ),
    ]

    def __str__(self):
        return self.author_name if self.author_name else "Author name missing"
