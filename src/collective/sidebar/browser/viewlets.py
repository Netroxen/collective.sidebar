# -*- coding: utf-8 -*-
from collective.sidebar.utils import crop
from collective.sidebar.utils import get_translated
from collective.sidebar.utils import get_user
from collective.sidebar.utils import hex_to_rgb
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.interfaces import IFolderish
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SidebarViewlet(ViewletBase):

    def is_anonymous(self):
        """
        Check if the user is anonymous.
        """
        return api.user.is_anonymous()

    def get_portal_url(self):
        """
        Return the portal URL.
        """
        return api.portal.get().absolute_url()

    def get_sidebar_colour(self):
        """
        Return the primary colour set by the user.
        """
        return api.portal.get_registry_record(
            'collective.sidebar.sidebar_colour',
        )

    def shadow_effects_enabled(self):
        """
        Check if shadow effects are enabled.
        """
        return api.portal.get_registry_record(
            'collective.sidebar.enable_shadows',
        )

    def cover_enabled(self):
        """
        Check if the page cover is enabled.
        """
        return api.portal.get_registry_record(
            'collective.sidebar.enable_cover',
        )

    def cookies_enabled(self):
        """
        Check if cookie features are enabled.
        """
        return api.portal.get_registry_record(
            'collective.sidebar.enable_cookies',
        )

    def get_navigation_position(self):
        """
        Return the navigation position that is set.
            - Left
            - Right
        """
        return api.portal.get_registry_record(
            'collective.sidebar.navigation_position',
        )

    def get_profile_position(self):
        """
        Return the profile position that is set.
            - Header
            - Sidebar
        """
        return api.portal.get_registry_record(
            'collective.sidebar.profile_position',
        )

    def get_rgb(self, colour, opacity):
        """
        Return an RGB or RGBA value from a hexadecimal code.
        """
        return hex_to_rgb(colour=colour, alpha=True, opacity=opacity)

    def get_user_data(self):
        """
        Return user information and portrait.
        """
        user = get_user()
        mtool = api.portal.get_tool('portal_membership')
        portrait = mtool.getPersonalPortrait(id=user[1])
        user_info = mtool.getMemberInfo(user[1])
        data = {
            'user_info': user_info,
            'portrait': portrait.absolute_url(),
        }
        return data

    def get_search_path(self, query=False):
        """
        Return a search URL using the SearchableText attribute.
        """
        portal_url = self.get_portal_url()
        if query:
            return '{0}/@@search?SearchableText='.format(portal_url)
        return '{0}/@@search'.format(portal_url)

    def get_navigation_root_url(self):
        """
        Return navigation root URL based on the language.
        """
        navigation_root = api.portal.get_navigation_root(self.context)
        return navigation_root.absolute_url()

    def get_language(self):
        """
        Return the current language.
        """
        return api.portal.get_current_language()

    def can_edit(self):
        """
        Check if the user can modify content.
        """
        permission = 'cmf.ModifyPortalContent'
        if api.user.has_permission(permission, obj=self.context):
            return True
        return False

    def can_manage_portal(self):
        """
        Check is user can manage the portal.
        """
        permission = 'cmf.ManagePortal'
        if api.user.has_permission(permission, obj=self.context):
            return True
        return False


class HeaderViewlet(SidebarViewlet):

    index = ViewPageTemplateFile('templates/header.pt')


class NavigationViewlet(SidebarViewlet):

    index = ViewPageTemplateFile('templates/sidebar.pt')

    def get_back(self):
        """
        Get link to parent.
        """
        parent = self.context.aq_parent
        if self.context == api.portal.get():
            return None
        if self.context.portal_type == 'LRF':
            return None
        try:
            if parent.default_page == self.context.id:
                if parent == api.portal.get_navigation_root(self.context):
                    return None
                else:
                    return parent.aq_parent.absolute_url()
        except AttributeError:
            pass
        return parent.absolute_url()

    def check_item(self, item):
        """
        Check if we want to have the given item in the navigation.
        """
        context = self.context
        if item.exclude_from_nav:
            return False
        try:
            if context.default_page == item.id:
                return False
        except AttributeError:
            pass
        return True

    def get_items(self, root=False):
        """
        Get folder contents and return.
        """
        context = self.context
        if root:
            context = api.portal.get_navigation_root(context)
        contents = []
        if IFolderish.providedBy(context):
            contents = context.getFolderContents()
        else:
            try:
                parent = context.aq_parent
                contents = parent.getFolderContents()
            except Exception:
                pass
        items = []
        for item in contents:
            if self.check_item(item):
                data = {
                    'title': item.Title,
                    'title_cropped': crop(item.Title, 100),
                    'url': item.getURL(),
                }
                items.append(data)
        return items

    def get_addable_types(self):
        """
        Get addable Content-Types.
        """
        context = self.context
        parent = context.aq_parent
        context_url = context.absolute_url()
        parent_url = parent.absolute_url()
        # Filter for Content-Types
        title_filter = []
        factories = api.content.get_view(
            'plone.contentmenu.factories',
            self.context,
            self.request,
        )
        addable_types = factories._addableTypesInContext(self.context)
        data = []
        for item in addable_types:
            title = item.id
            if title in title_filter:
                pass
            else:
                url = context_url
                try:
                    if parent.default_page == context.id:
                        url = parent_url
                except AttributeError:
                    pass
                url = '{0}/++add++{1}'.format(url, title)
                data.append({'title': get_translated(title, self), 'url': url})
        return data

    def get_folder_contents_url(self):
        """
        Get URL to folder_contents.
        """
        context = self.context
        parent = context.aq_parent
        context_url = context.absolute_url() + '/folder_contents'
        parent_url = parent.absolute_url() + '/folder_contents'
        try:
            if parent.default_page == context.id:
                return parent_url
        except AttributeError:
            pass
        if IFolderish.providedBy(context):
            return context_url
        else:
            return parent_url


class NavigationAJAX(BrowserView):

    def __call__(self, render):
        context = self.context
        request = self.request
        if render:
            return self.render_viewlet(context, request)
        return None

    def render_viewlet(self, context, request):
        navigation = NavigationViewlet(context, request, None, None)
        return navigation.render()


class CoverViewlet(SidebarViewlet):

    index = ViewPageTemplateFile('templates/cover.pt')
