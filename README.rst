*********
sc.banner
*********

.. contents:: Conteúdo
   :depth: 2

Life, the Universe, and Everything
----------------------------------

A Dexterity-based content type representing a banner: an image with a link.

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/simplesconsultoria/sc.banner.png?branch=master
    :target: http://travis-ci.org/simplesconsultoria/sc.banner

.. image:: https://coveralls.io/repos/simplesconsultoria/sc.banner/badge.png?branch=master
    :target: https://coveralls.io/r/simplesconsultoria/sc.banner

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

Don't Panic
-----------

Installation
^^^^^^^^^^^^

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        sc.banner

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``sc.banner`` and click the 'Activate' button.

.. Note::
    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.

Usage
^^^^^

A Banner is a content type with the same behavior of the standard Link,
containing an aditional image field.

When accessing a Banner, you have two behaviors: if the user has permission to
edit the object, she will see the default view of the object with a status
message on top.

If the user has no permission to edit the object, she will be redirected to
the URL stored in the Banner.

A Banner should point to an external URL and only 'http' and 'https' schemes
are allowed by design.

.. _`opening a support ticket`: https://github.com/simplesconsultoria/sc.banner/issues
