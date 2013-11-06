# -*- coding: utf-8 -*-

from five import grok
from plone import api
from sc.banner.interfaces import IBanner

grok.templatedir('templates')


class View(grok.View):
    grok.context(IBanner)
    grok.require('zope2.View')
    grok.name('banner_view')


class BannerRedirectView(grok.View):
    grok.context(IBanner)
    grok.name('banner_redirect_view')
    grok.require('zope2.View')

    def render(self):
        """Redirect to the target URL if, and only if:
        - redirect_links property is enabled in portal_properties/site_properties
        - current user doesn't have permission to edit the Banner
        """
        context = self.context
        ptool = api.portal.get_tool('portal_properties')
        mtool = api.portal.get_tool('portal_membership')

        redirect_links = getattr(ptool.site_properties, 'redirect_links', False)
        can_edit = mtool.checkPermission('Modify portal content', context)

        if redirect_links and not can_edit:
            return context.REQUEST.RESPONSE.redirect(context.remote_url)
        else:
            return context.restrictedTraverse('@@banner_view')()
