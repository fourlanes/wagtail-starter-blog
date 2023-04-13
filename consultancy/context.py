import os
from django.conf import settings

from wagtail.models import Site

from home.models import HomePage


def get_current_page(request):
    try:
        # this try is here to protect against 500 errors when there is a 404 error
        # taken from https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailcore/views.py#L17
        path_components = [component for component in request.path.split("/") if component]
        current_page, args, kwargs = Site.find_for_request(request).root_page.specific.route(request, path_components)
        return current_page
    except Exception:
        return None


def get_html_title(request):
    current_page = get_current_page(request)
    # Try getting the page name in a format like:
    # Page title - Site title
    try:
        html_title = ""
        if current_page.seo_title:
            html_title += current_page.seo_title
        else:
            html_title += current_page.title
        if not isinstance(current_page, HomePage):
            html_title += " - "
            html_title += str(Site.find_for_request(request).site_name)
    except Exception:
        # Probably 404 or wagtail admin
        html_title = ""

    return html_title


def globals(request):

    if request.path.startswith("/admin/") or request.path.startswith("/django-admin/"):
        return {}

    html_title = get_html_title(request)
    current_page = get_current_page(request)
    is_home = isinstance(current_page, HomePage)

    return {
        "global": {
            "DEBUG": bool(os.getenv("DEBUG", False)),
            "is_home": is_home,
            "site_name": Site.find_for_request(request).site_name or settings.WAGTAIL_SITE_NAME,
            "html_title": html_title,
        },
    }
