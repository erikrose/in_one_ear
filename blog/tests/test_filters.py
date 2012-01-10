from in_one_ear.blog.templatetags.rst2html import rst2html


def test_rst2html():
    """Make sure rst2html renders restructured text."""
    assert '<em>improbable</em>' in rst2html('*improbable*')
