# -*- coding: utf-8 -*-

from plone.browserlayer.utils import registered_layers
from plone.testing.z2 import Browser
from sc.banner.config import PROJECTNAME
from sc.banner.interfaces import IBrowserLayer
from sc.banner.testing import INTEGRATION_TESTING

import unittest


class BaseTestCase(unittest.TestCase):
    """Base test case to be used by other tests."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.wt = self.portal['portal_workflow']
        self.st = self.portal['portal_setup']


class TestInstall(BaseTestCase):
    """Ensure product is properly installed."""

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_browser_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())

    def test_static_resource_grokker(self):
        """Grok does not register automatically the static resources anymore
        see: http://svn.zope.org/five.grok/trunk/src/five/grok/meta.py?rev=123298&r1=112163&r2=123298
        """
        portal = self.layer['portal']
        app = self.layer['app']

        browser = Browser(app)
        portal_url = portal.absolute_url()

        browser.open('%s/++resource++sc.banner' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')


class TestUninstall(BaseTestCase):
    """Ensure product is properly uninstalled."""

    def setUp(self):
        BaseTestCase.setUp(self)
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_browser_layer_removed_uninstalled(self):
        self.qi.uninstallProducts(products=[PROJECTNAME])
        self.assertNotIn(IBrowserLayer, registered_layers())
