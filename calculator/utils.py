""" Utility file; contains generic methods/helpers usable everywhere
"""

from markdown import markdown
from calculator.config import MARKDOWN_EXTENSIONS


def markdownify(md):
    """ Transform a markdown string into HTML
    """
    return markdown(md, extensions=MARKDOWN_EXTENSIONS)
