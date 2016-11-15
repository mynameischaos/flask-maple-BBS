
from flask import Blueprint
from flask_login import login_required
from maple.helpers import register_api
from .views import CollectAPI, LikeAPI, FollowAPI, CollectDetailAPI
from .views import collect_following

site = Blueprint('mine', __name__)
site.add_url_rule('/collect/following',
                  view_func=login_required(collect_following))

register_api(site, CollectAPI, 'collect', '/collect', 'collectId')
register_api(site, CollectDetailAPI, 'collect_detail', '/collect/detail',
             'collectId')

# register_api(FollowAPI, 'follow', '/follow', 'type', 'string')

follow_view = FollowAPI.as_view('follow')
site.add_url_rule('/follow',
                  defaults={'type': 'topic'},
                  view_func=follow_view,
                  methods=['GET'])
site.add_url_rule('/follow/<type>',
                  view_func=follow_view,
                  methods=['GET', 'POST', 'DELETE'])

like_view = LikeAPI.as_view('like')
site.add_url_rule('/like/<int:replyId>',
                  view_func=like_view,
                  methods=['POST', 'DELETE'])
