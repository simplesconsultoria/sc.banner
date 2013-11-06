# -*- coding: utf-8 -*-

from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from sc.banner import _
from zope import schema
from zope.interface import Interface


class IBrowserLayer(Interface):
    """Browser layer specific for this add-on.
    """


class IBanner(form.Schema):
    """A content type representing a banner."""

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u''),
        required=True,
    )

    remote_url = schema.ASCIILine(
        title=_(u'Link'),
        description=_(u''),
        required=True,
    )
