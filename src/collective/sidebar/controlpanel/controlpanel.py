# -*- coding: utf-8 -*-
from collective.sidebar import _
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

    enable_shadows = schema.Bool(
        title=_(u'controlpanel_enable_shadows_title',
                default='Enable Shadow Effects'),
        description=_(u'controlpanel_enable_shadows_description',
                      default=u'Enable or disable the navigation shadow effects. Note: IE 11, FF 60, Chrome 49 and above only...'),  # noqa: 501
        required=False,
        default=True,
    )

    fieldset(
        _(u'controlpanel_fieldset_navigation',
          default=u'Navigation'),
        fields=('enable_cover', 'profile_section'),
    )

    enable_cover = schema.Bool(
        title=_(u'controlpanel_enable_cover_title',
                default='Fade-In Cover'),
        description=_(u'controlpanel_enable_cover_description',
                      default=u'Enable or disable the navigation fade-in cover when open.'),  # noqa: 501
        required=False,
        default=True,
    )

    profile_section = schema.Bool(
        title=_(u'controlpanel_profile_section_title',
                default='Profile Section'),
        description=_(u'controlpanel_profile_section_description',
                      default=u'Enable or disable the navigation profile section.'),  # noqa: 501
        required=False,
        default=True,
    )


class ControlPanelEditForm(RegistryEditForm):
    schema = IControlPanel
    schema_prefix = 'collective.sidebar'
    label = _(u'collective_sidebar_title', default=u'Collective Sidebar')


ControlPanelView = layout.wrap_form(
    ControlPanelEditForm,
    ControlPanelFormWrapper,
)
