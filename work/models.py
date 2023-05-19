from django.db import models  # noqa: F401
from django.contrib.contenttypes.models import ContentType

from wagtail.models import Page

from common.mixins import ContactUsFooterMixin, CustomMetadataPageMixin
from common.utils import ContactUsFooterPanels
from blog.models import ArticlePage, ArticleTopic


class WorkListing(ContactUsFooterMixin, CustomMetadataPageMixin, Page):
    class Meta:
        verbose_name = "Work Listing"

    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.ArticlePage"]
    max_count = 1

    content_panels = Page.content_panels + [
        ContactUsFooterPanels(),
    ]

    def get_context(self, request):
        context = super(WorkListing, self).get_context(request)

        article_content_type = ContentType.objects.get_for_model(ArticlePage)
        context["topics"] = (
            ArticleTopic.objects.filter(tagged_article__content_object__content_type=article_content_type)
            .distinct()
            .order_by("name")
        )

        return context
