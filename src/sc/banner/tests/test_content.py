# -*- coding: utf-8 -*-

from plone import api
from plone.app.referenceablebehavior.referenceable import IReferenceable
from plone.dexterity.interfaces import IDexterityFTI
from plone.uuid.interfaces import IAttributeUUID
from sc.banner.interfaces import IBanner
from sc.banner.testing import INTEGRATION_TESTING
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ContentTypeTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        with api.env.adopt_roles(['Manager']):
            self.portal.invokeFactory('Folder', 'test-folder')
            self.folder = self.portal['test-folder']

        self.folder.invokeFactory('Banner', 'Banner')
        self.Banner = self.folder['Banner']

    def test_adding(self):
        self.assertTrue(IBanner.providedBy(self.Banner))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Banner')
        self.assertIsNotNone(fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Banner')
        schema = fti.lookupSchema()
        self.assertEqual(IBanner, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Banner')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IBanner.providedBy(new_object))

    def test_is_referenceable(self):
        self.assertTrue(IReferenceable.providedBy(self.Banner))
        self.assertTrue(IAttributeUUID.providedBy(self.Banner))
