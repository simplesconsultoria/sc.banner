# -*- coding: utf-8 -*-

from sc.banner.config import PROJECTNAME
from sc.banner.testing import INTEGRATION_TESTING
from sc.banner.interfaces import IBrowserLayer
from plone.browserlayer.utils import registered_layers

import unittest


class TestBrowserLayer(unittest.TestCase):
    """Ensure browser layer is installed and uninstalled properly."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())

    def test_uninstalled(self):
        self.qi.uninstallProducts(products=[PROJECTNAME])
        self.assertNotIn(IBrowserLayer, registered_layers())
