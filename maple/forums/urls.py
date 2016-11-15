
from flask import Blueprint
from flask_login import login_required
from .views import (index, forums, notice, userlist, message, about, help,
                    order, contact)

site = Blueprint('forums', __name__)

notice = login_required(notice)
userlist = login_required(userlist)
message = login_required(message)

site.add_url_rule('/', view_func=index)
site.add_url_rule('/index', view_func=forums)
site.add_url_rule('/notices', view_func=notice)
site.add_url_rule('/userlist', view_func=userlist)
site.add_url_rule('/about', view_func=about)
site.add_url_rule('/help', view_func=help)
site.add_url_rule('/contact', view_func=contact)
site.add_url_rule('/order', view_func=order, methods=['POST'])
site.add_url_rule('/messages/<receId>', view_func=message, methods=['POST'])
