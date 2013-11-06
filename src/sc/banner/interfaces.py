# -*- coding: utf-8 -*-

from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from sc.banner import _
from zope import schema
from zope.interface import Interface

import urlparse


class IBrowserLayer(Interface):
    """Browser layer specific for this add-on.
    """


def is_valid_url(value):
    """Return True is the URL scheme is http or https.
    """
    url = urlparse.urlparse(value)
    return url.scheme in ['http', 'https']


class IBanner(form.Schema):
    """A content type representing a banner."""

    image = NamedBlobImage(
        title=_(u'Image'),
        description=_(u''),
        required=True,
    )

    remote_url = schema.ASCIILine(
        title=_(u'URL'),
        description=_(u'Must be an absolute URL. Valid schemes are http and https only.'),
        required=True,
        constraint=is_valid_url,
    )
