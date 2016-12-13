from plone.autoform import directives
from plone.dexterity.content import Item
from plone.supermodel import directives as supermodel_directives
from plone.supermodel import model
from zope import schema
from zope.interface import implements

from .. import _


class IPlominoHidewhen(model.Schema):
    """ Plomino hide-when schema
    """

    directives.widget('formula', klass='plomino-formula')
    formula = schema.Text(
        title=_('CMFPlomino_label_HidewhenFormula', default="Formula"),
        description=_('CMFPlomino_help_HidewhenFormula',
            default='If returning True, the block will be hidden.'),
        required=True,
        default=u"False",
    )

    isDynamicHidewhen = schema.Bool(
        title=_('CMFPlomino_label_isDynamicHidewhen',
            default="Dynamic Hide-when"),
        description=_('CMFPlomino_help_isDynamicHidewhen',
            default="Hide-when are evaluated dynamically when the user enters"
            " information"),
        required=True,
        default=False,
    )

    # # ADVANCED
    # supermodel_directives.fieldset(
    #     'advanced',
    #     label=_(u'Advanced'),
    #     fields=(
    #         'formula',
    #     ),
    # )




class PlominoHidewhen(Item):
    implements(IPlominoHidewhen)
