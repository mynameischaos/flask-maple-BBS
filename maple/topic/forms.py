
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length
from flask_babelex import lazy_gettext as _
from maple.forums.models import Board


class TopicForm(Form):
    title = StringField(_('Title:'), [DataRequired(), Length(min=4, max=36)])
    content = TextAreaField(_('Content:'), [DataRequired(), Length(min=6)])
    category = SelectField(
        _('Category:'),
        choices=[(b.id, b.board + '   --' + b.parent_board)
                 for b in Board.query.all()],
        coerce=int)
    tags = StringField(_('Tags:'), [DataRequired(), Length(min=2, max=36)])
    choice = SelectField('choice',
                         choices=[(1, 'Markdown'), (2, 'Default')],
                         coerce=int)


class ReplyForm(Form):
    content = TextAreaField(_('Content:'), [DataRequired()])
