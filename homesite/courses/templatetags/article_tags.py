from django import template
from django.utils.safestring import mark_safe
from markdown import markdown
import re

register = template.Library()

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'codehilite',
]

MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS = {
    'codehilite': {'linenums':True}
}


def cheater(content):

    """
    Until AWS s3 instance is set up or shared instance is created this 
    will replace the media links with their absolute destinations
    """

    content = re.sub(r'(!\[[^\]]*]\()([^\)]+\))', r'\1http://167.99.167.145\2', content)


    return content


@register.filter(name='to_HTML')
def markdown_to_HTML(content):

    content = cheater(content)

    md = markdown(
        text=content,
        extensions=MARKDOWNX_MARKDOWN_EXTENSIONS,
        extension_configs=MARKDOWNX_MARKDOWN_EXTENSION_CONFIGS)

    return md