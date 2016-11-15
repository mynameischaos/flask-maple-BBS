
from flask_wtf import Form
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_babelex import lazy_gettext as _


class SortForm(Form):
    display = SelectField(
        _('Choice'),
        coerce=int,
        choices=[(0, _('All Topics')), (1, _('One Day')), (2, _('One Week')), (
            3, _('One Month'))])
    sort = SelectField('Sort',
                       coerce=int,
                       choices=[(0, _('Publish')), (1, _('Author'))])
    st = SelectField('Up and Down',
                     coerce=int,
                     choices=[(0, _('Desc')), (1, _('Asc'))])


class SearchForm(Form):
    search = StringField(_('search'), validators=[DataRequired()])


class MessageForm(Form):
    message = TextAreaField(_('message'), validators=[DataRequired()])
