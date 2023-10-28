from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.panels import FieldPanel

from blog.models import ArticleTopic


class ArticleTopicViewSet(SnippetViewSet):
    model = ArticleTopic

    panels = [
        FieldPanel("name"),
    ]


register_snippet(ArticleTopicViewSet)
