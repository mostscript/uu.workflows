from zope.lifecycleevent import modified
from DateTime import DateTime #zope2 DateTime
from Products.CMFCore.utils import getToolByName


_true = lambda a,b: a==b==True
all_true = lambda seq: reduce(_true, seq)
has_log = lambda wf,o: wf.isActionSupported(o, 'log')


def history_log(context, message, set_modified=True):
    """
    Use 'log' workflow transition, if available, to leave a log message
    comment.  This may be used by event handlers for a context needing to
    write a log message to content history.
    """
    if isinstance(message, unicode):
        message = message.encode('utf-8')   # if unicode, assume utf-8
    message = str(message)                  # if message is a number of tuple
    wtool = getToolByName(context, 'portal_workflow')
    wflows = wtool.getWorkflowsFor(context)
    has_log_transition = all_true([has_log(wf, context) for wf in wflows])
    if has_log_transition:
        wtool.doActionFor(context, 'log', comment=message)
    if set_modified:
        context.modification_date = DateTime() # == now
        modified(context) #notify to reindex object.

