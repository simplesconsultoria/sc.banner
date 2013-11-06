# -*- coding: utf-8 -*-

from sc.banner.interfaces import IBanner
from five import grok
from plone.dexterity.content import Container


class Banner(Container):
    """A content type representing a banner."""
    grok.implements(IBanner)
