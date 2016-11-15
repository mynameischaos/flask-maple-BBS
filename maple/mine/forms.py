
from flask_wtf import Form
from wtforms import (StringField, TextAreaField, SelectField, PasswordField,
                     RadioField)
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired
from flask_babelex import lazy_gettext as _


class CollectForm(Form):
    name = StringField(_('Name:'), [DataRequired()])
    description = TextAreaField(_('Description:'))
    is_privacy = RadioField('Is_privacy:',
                            choices=[(0, 'privacy'), (1, 'public')],
                            coerce=int)
