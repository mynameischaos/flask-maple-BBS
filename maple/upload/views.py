
from flask import (url_for, redirect, flash, send_from_directory, current_app)
from flask_maple.forms import flash_errors
from flask_login import login_required
from .forms import AvatarForm
from .controls import UploadModel
import os


@login_required
def avatar():
    form = AvatarForm()
    if form.validate_on_submit():
        UploadModel.avatar(form)
        flash('上传成功', 'success')
        return redirect(url_for('setting.setting'))
    else:
        if form.errors:
            flash_errors(form)
        return redirect(url_for('setting.setting'))


def avatar_file(filename):
    avatar_path = os.path.join(current_app.static_folder,
                               current_app.config.get('AVATAR_FOLDER',
                                                      'avatars/'))
    if not os.path.exists(os.path.join(avatar_path, filename)):
        avatar_path = os.path.join(current_app.static_folder, 'images/')
        filename = 'default_avatar.jpg'
    return send_from_directory(avatar_path, filename)
