# -*- coding: utf-8 -*-

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2


def create_image(width, height):
    from PIL import Image
    from StringIO import StringIO
    size, color = (width, height), (255, 0, 0)
    image = Image.new('RGBA', size, color)
    output = StringIO()
    image.save(output, format='PNG')
    return output.getvalue()


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import sc.banner
        self.loadZCML(package=sc.banner)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'sc.banner:default')
        # the following image is used on Robot Framework tests
        open('/tmp/banner.jpg', 'w').write(create_image(728, 90))


FIXTURE = Fixture()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='sc.banner:Integration')

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='sc.banner:Functional')

ROBOT_TESTING = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='sc.banner:Robot',
)
