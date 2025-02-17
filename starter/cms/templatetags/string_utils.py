import os

import bleach
import uuid
import re

from bleach.css_sanitizer import CSSSanitizer

from django import template
from django.utils import formats
from django.utils.text import Truncator
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

from wagtail.rich_text import expand_db_html, RichText

register = template.Library()

WYSIWYG_LIST = list(bleach.ALLOWED_TAGS) + [
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hr",
    "p",
    "img",
    "iframe",
    "figure",
    "figcaption",
    "cite",
    "blockquote",
    "pre",
    "table",
    "tr",
    "td",
    "th",
    "span",
    "sup",
    "sub",
    "code",
    "blockquote",
    "abbr",
]
MINIMAL_LIST = list(bleach.ALLOWED_TAGS) + [
    "p",
]
ATTRS = bleach.ALLOWED_ATTRIBUTES
ATTRS["img"] = ["alt", "src", "class", "width", "height"]
ATTRS["iframe"] = [
    "src",
    "width",
    "height",
    "frameborder",
    "title",
    "webkitallowfullscreen",
    "mozallowfullscreen",
    "allowfullscreen",
]

# Allow style attribute on span
ATTRS["span"] = ["style", "data-type", "data-id"]

# Allow class for cite on p
ATTRS["p"] = ["class"]

# Allow style attribute on p
ATTRS["p"] = ["style"]

# Allow title attribute on attr
ATTRS["abbr"] = ["title"]

# Allow only text alignment and justification on styles
STYLES = ["text-decoration", "text-align"]

# Allow some table attributes
ATTRS["table"] = ["id", "summary", "title"]
ATTRS["th"] = ["id", "colspan", "rowspan", "width"]
ATTRS["td"] = ["id", "colspan", "rowspan"]

css_sanitizer = CSSSanitizer(allowed_css_properties=STYLES)


@register.filter(name="wysiwyg_tags")
def wysiwyg_tags(text):
    clean = bleach.clean(
        text, tags=WYSIWYG_LIST, attributes=ATTRS, css_sanitizer=css_sanitizer, strip=True, strip_comments=True
    )

    return mark_safe(re.sub(r"<p>\s*</p>", "", clean))


@register.filter
def rich_text(value):
    if isinstance(value, RichText):
        # passing a RichText value through the |richtext filter should have no effect
        return str(value)
    elif value is None:
        html = ""
    else:
        html = expand_db_html(value)

    return mark_safe(html)


@register.filter
def content(value):
    return wysiwyg_tags(rich_text(value))


@register.simple_tag
def uid():
    return str(uuid.uuid4())[:6]


@register.simple_tag(takes_context=True)
def uid_url(context, obj):
    try:
        request = context["request"]
        return "%s://%s/%s" % (request.scheme, request.get_host(), obj.uuid)
    except Exception:
        try:
            request = context["request"]
            return "%s://%s%s" % (request.scheme, request.get_host(), obj.url)
        except Exception:
            return ""


def sizeof_fmt(num, suffix="B"):
    for unit in ["", "k", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Y", suffix)


@register.filter
def file_info(file):
    try:
        return "%s %s" % (os.path.splitext(file.url)[1][1:].upper(), sizeof_fmt(file.file.size))
    except Exception:
        return file.title


@register.filter
def file_label(file):
    try:
        return "%s | %s %s" % (file.title, os.path.splitext(file.url)[1][1:].upper(), sizeof_fmt(file.file.size))
    except Exception:
        return file.title


@register.filter
def file_exists(file):
    try:
        if file.size:
            return True
    except:  # noqa: E722
        return False


@register.filter(expects_localtime=True, is_safe=False)
def format_date(start, end=None):
    """Check that years are not the same and format date field."""

    if start in (None, "") or end in (None, ""):
        return ""

    if formats.date_format(start, "Y") == formats.date_format(end, "Y"):
        return formats.date_format(start, "d F") + " - " + formats.date_format(end, "d F, Y")
    else:
        return formats.date_format(start, "d F, Y") + " - " + formats.date_format(end, "d F, Y")


# Helper function for content_excerpt
@register.filter
def return_content(content):
    return mark_safe(Truncator(strip_tags(str(content))).words(30))


@register.filter
def string_start(value, up_to_character="-"):
    return value.split(up_to_character)[0]


@register.simple_tag
def prepend_with_char(value, string, char="."):
    if string:
        return "%s%s%s" % (string, char, value)
    return value


@register.filter
def add_string(stringA, stringB):
    """concatenate stringA & stringB"""
    return str(stringA) + str(stringB)
