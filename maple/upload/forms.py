
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_babelex import lazy_gettext as _


class AvatarForm(Form):
    avatar = FileField(
        _('Upload Avatar:'),
        validators=[FileRequired(), FileAllowed(
            ['jpg', 'png'], '上传文件只能为图片且图片格式为jpg,png')])
