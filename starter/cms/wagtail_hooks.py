from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel

from wagtail import hooks

from starter.cms.models import ArticleTopic


@hooks.register("insert_global_admin_css")
def global_admin_css():
    """Add /static/css/admin.css to the admin."""
    return format_html('<link rel="stylesheet" href="{}">', static("css/admin.css"))


class ArticleTopicViewSet(SnippetViewSet):
    model = ArticleTopic

    panels = [
        FieldPanel("name"),
    ]


register_snippet(ArticleTopicViewSet)
