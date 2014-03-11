from zope.interface import implements
from plone.app.workflow.interfaces import ISharingPageRole
from Products.CMFPlone import PloneMessageFactory as _


class FormEntryRole(object):
    implements(ISharingPageRole)
    title = _(u'title_can_enter_data', default=u'Can enter data')
    required_permission = 'Enter Data'


class ManagerRole(object):
    implements(ISharingPageRole)
    title = _(u'title_can_manage', default=u'Can manage')
    required_permission = 'Manage portal'

