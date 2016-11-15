
from flask import Blueprint
from .views import setting, password, privacy, babel

site = Blueprint('setting', __name__)

site.add_url_rule('', view_func=setting, methods=['GET', 'POST'])
site.add_url_rule('/profile', view_func=setting, methods=['GET', 'POST'])
site.add_url_rule('/password', view_func=password, methods=['GET', 'POST'])
site.add_url_rule('/privacy', view_func=privacy, methods=['GET', 'POST'])
site.add_url_rule('/babel', view_func=babel, methods=['GET', 'POST'])
