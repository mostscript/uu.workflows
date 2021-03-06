from zope.component.hooks import getSite
from Acquisition import aq_parent
from DateTime import DateTime  # zope2 DateTime
from plone.app.contentrules.handlers import _status as rule_status
from Products.CMFCore.utils import getToolByName


_true = lambda a, b: a == b and b
all_true = lambda seq: reduce(_true, seq)
has_log = lambda wf, o: wf.isActionSupported(o, 'log')


def history_log(context, message, set_modified=True):
    """
    Use 'log' workflow transition, if available, to leave a log message
    comment.  This may be used by event handlers for a context needing to
    write a log message to content history.
    """
    parent = aq_parent(context)
    portal = getSite()  # need site as context in case of non-aq-wrapped context
    if isinstance(message, unicode):
        message = message.encode('utf-8')   # if unicode, assume utf-8
    message = str(message)                  # if message is a number of tuple
    wtool = getToolByName(portal, 'portal_workflow')
    wflows = wtool.getWorkflowsFor(context)
    has_log_transition = all_true([has_log(wf, context) for wf in wflows])
    if has_log_transition:
        if parent is None:
            context = context.__of__(portal)  # wrap for wtool to deal with
        wtool.doActionFor(context, 'log', comment=message)
        # we do not expect content rules to trigger on log transitions, but
        # plone.app.contentrules has a frustrating bug we now work around:
        #  https://goo.gl/zTkbKB
        rule_status.rule_filter.executed = set()
    if set_modified:
        context.modification_date = DateTime()  # == now
        if parent is not None:
            context.reindexObject()

