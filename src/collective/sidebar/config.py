# -*- coding: utf-8 -*-
from collective.sidebar import _
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


package = 'collective.sidebar'

NAVIGATION_POSITIONS = SimpleVocabulary([
    SimpleTerm(value=u'right', title=_(u'Right')),
    SimpleTerm(value=u'left', title=_(u'Left')),
])

PROFILE_POSITIONS = SimpleVocabulary([
    SimpleTerm(value=u'header', title=_(u'Header')),
    SimpleTerm(value=u'sidebar', title=_(u'Sidebar')),
])
