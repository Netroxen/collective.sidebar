# -*- coding: utf-8 -*-
from collective.sidebar import _
from collective.sidebar.config import NAVIGATION_POSITIONS
from collective.sidebar.config import PROFILE_POSITIONS
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.supermodel.directives import fieldset
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IControlPanel(Interface):

    sidebar_colour = schema.TextLine(
        title=_(u'controlpanel_sidebar_colour_title',
                default='Sidebar Colour'),
        description=_(u'controlpanel_sidebar_colour_description',
                      default=u'Enter a primary colour to be used for the header and navigation. e.g. #007EB6'),  # noqa: 501
        required=True,
        default=u'#007EB6',
    )

    enable_cookies = schema.Bool(
        title=_(u'controlpanel_enable_cookies_title',
                default='Enable Cookie Features'),
        description=_(u'controlpanel_enable_cookies_description',
                      default=u'Enable or disable cookies for sidebar enhancements. e.g. Sidebar-Locking'),  # noqa: 501
        required=False,
        default=True,
    )

    fieldset(
        _(u'controlpanel_fieldset_effects',
          default=u'Effects'),
        fields=('enable_cover', 'enable_shadows'),
    )

    enable_cover = schema.Bool(
        title=_(u'controlpanel_enable_cover_title',
                default='Fade-In Cover'),
        description=_(u'controlpanel_enable_cover_description',
                      default=u'Enable or disable the page cover when the sidebar is open.'),  # noqa: 501
        required=False,
        default=True,
    )

    enable_shadows = schema.Bool(
        title=_(u'controlpanel_enable_shadows_title',
                default='Enable Shadow Effects'),
        description=_(u'controlpanel_enable_shadows_description',
                      default=u'Enable or disable the navigation box-shadow effects.'),  # noqa: 501
        required=False,
        default=True,
    )

    fieldset(
        _(u'controlpanel_fieldset_navigation',
          default=u'Navigation'),
        fields=('navigation_position', 'profile_position'),
    )

    navigation_position = schema.Choice(
        title=_(u'controlpanel_navigation_position_title',
                default='Navigation Position'),
        description=_(u'controlpanel_navigation_position_description',
                      default=u'Display the navigation on the left or right side of the screen.'),  # noqa: 501
        vocabulary=NAVIGATION_POSITIONS,
        required=True,
        default=u'right',
    )

    profile_position = schema.Choice(
        title=_(u'controlpanel_profile_position_title',
                default='Profile Position'),
        description=_(u'controlpanel_profile_position_description',
                      default=u'Display the profile section in the header or sidebar.'),  # noqa: 501
        vocabulary=PROFILE_POSITIONS,
        required=True,
        default=u'sidebar',
    )


class ControlPanelEditForm(RegistryEditForm):
    schema = IControlPanel
    schema_prefix = 'collective.sidebar'
    label = _(u'collective_sidebar_title', default=u'Collective Sidebar')


ControlPanelView = layout.wrap_form(
    ControlPanelEditForm,
    ControlPanelFormWrapper,
)
