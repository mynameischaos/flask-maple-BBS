
from flask import Blueprint
from .views import tag, rss

site = Blueprint('tag', __name__)

site.add_url_rule('', view_func=tag, defaults={'tag': None})
site.add_url_rule('/<tag>', view_func=tag)
site.add_url_rule('/<tag>/feed', view_func=rss)
