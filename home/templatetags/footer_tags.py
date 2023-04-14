from django import template

from common.models import ContactUsFooter

register = template.Library()


@register.inclusion_tag("tags/scaffold/contact_us_footer.html", takes_context=True)
def contact_us_footer(context):
    self = context.get("self")

    if not self.show_contact_us_footer:
        return {"self": None, "request": context.get("request")}

    instance = ContactUsFooter.load(request_or_site=context["request"])

    return {
        "self": instance,
        "request": context.get("request"),
    }
