from zope.interface import Interface
from zope import schema


class ILoggable(Interface):
    """
    Marker interface for an object for which a 'log' workflow transition
    may be available for use by uu.workflow.utils.history_log()
    
    May also be used as a marker for a logging or journal view on such a
    context.
    """


class IJournalSchema(Interface):
    """
    Interface for form schema of log-message journal entries.
    """
    
    message = schema.Text(
        title=u'Message text',
        description=u'The text of the journal message you wish to log.',
        required=True,
        )

