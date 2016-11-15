
from flask import Blueprint
from .views import avatar, avatar_file

site = Blueprint('upload', __name__)

site.add_url_rule('/avatar', view_func=avatar, methods=['POST'])
site.add_url_rule('/avatars/<filename>', view_func=avatar_file)
