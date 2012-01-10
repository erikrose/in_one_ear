from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from docutils.core import publish_parts
from docutils.writers import html4css1


register = template.Library()


@register.filter
@stringfilter
def rst2html(rst):
    """Render reStructured Text into HTML.

    Disable dangerous things, like file inclusion and raw HTML.

    """
    # Keep authors from spilling the contents of local files into the post
    # or abusing raw HTML:
    secure_settings = {'file_insertion_enabled': 0,
                       'raw_enabled': 0,
                       'initial_header_level': 2,
                       '_disable_config': 1}
    return mark_safe(publish_parts(
            rst,
            writer=html4css1.Writer(),
            settings_overrides=secure_settings)['html_body'])
