#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: admin.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-05-31 21:42:11 (CST)
# Last Update:星期日 2016-8-7 18:45:36 (CST)
#          By:
# Description:
# **************************************************************************
from maple import db, app
from maple.forums.models import Board, Count, Notice
from maple.tag.models import Tags
from maple.user.models import Role
from maple.permission.models import Permiss, Route
from flask import abort
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import Form
from flask_principal import Permission, RoleNeed

admin = Admin(app,
              url=app.config.get('ADMIN_URL', '/admin'),
              name='Admin',
              template_mode='bootstrap3')


class BaseForm(Form):
    def __init__(self, formdata=None, obj=None, prefix=u'', **kwargs):
        self._obj = obj
        super(BaseForm, self).__init__(formdata=formdata,
                                       obj=obj,
                                       prefix=prefix,
                                       **kwargs)


class BaseModelView(ModelView):

    session = db.session
    page_size = 10
    can_view_details = True
    form_base_class = BaseForm

    def is_accessible(self):
        permission = Permission(RoleNeed('super'))
        return permission.can()

    def inaccessible_callback(self, name, **kwargs):
        abort(404)


class BoardModelView(BaseModelView):
    column_list = ['id', 'parent_board', 'board', 'description', 'rank',
                   'count.topics', 'count.all_topics']
    column_labels = {'count.topics': '主题', 'count.all_topics': '所有主题'}
    form_excluded_columns = ('topics')


class CountModelView(BaseModelView):
    column_list = ['id', 'board', 'topics', 'all_topics', 'drafts', 'collects',
                   'inviteds', 'follows']
    inline_models = [(Board, dict(form_excluded_columns=['topics']))]


class PermissView(BaseModelView):
    column_display_pk = True
    column_list = ['id', 'name', 'roles', 'method', 'routes', 'is_allow']
    column_editable_list = ['is_allow', 'method']
    form_choices = {'method': [('GET', 'GET'), ('POST', 'POST'),
                               ('PUT', 'PUT'), ('DELETE', 'DELETE')]}


class RoleView(BaseModelView):
    column_display_pk = True
    column_list = ['id', 'name', 'permissions', 'parents', 'children']


def get_list():
    endpoints = []
    for rule in app.url_map.iter_rules():
        endpoints.append((rule.endpoint, rule.endpoint))
    return endpoints


class RouteView(BaseModelView):
    column_display_pk = True
    column_list = ['id', 'permissions', 'endpoint', 'rule']
    form_choices = {'endpoint': get_list()}


class TagsModelView(BaseModelView):
    column_searchable_list = ['tagname']
    column_list = ['tagname', 'parents', 'children', 'summary', 'time']
    form_excluded_columns = ('tags', 'users', 'topics', 'followers')


class NoticeView(BaseModelView):
    column_filters = ['category', 'rece_user.username', 'send_user.username',
                      'is_read', 'publish']
    column_searchable_list = ['content']
    column_editable_list = ['is_read']
    form_widget_args = {'content': {'rows': 10}}


admin.add_view(BoardModelView(Board,
                              db.session,
                              name='管理版块',
                              endpoint='admin_boards',
                              category='管理论坛'))
admin.add_view(CountModelView(Count,
                              db.session,
                              name='管理统计',
                              endpoint='admin_counts',
                              category='管理论坛'))
admin.add_view(TagsModelView(Tags,
                             db.session,
                             name='管理节点',
                             endpoint='admin_tags',
                             category='管理论坛'))
admin.add_view(RoleView(Role,
                        db.session,
                        name='管理用户组',
                        endpoint='admin_role_permission',
                        category='权限管理'))
admin.add_view(PermissView(Permiss,
                           db.session,
                           name='管理权限',
                           endpoint='admin_permiss',
                          category='权限管理'))
admin.add_view(RouteView(Route,
                         db.session,
                         name='管理视图',
                         endpoint='admin_route',
                         category='权限管理'))
admin.add_view(NoticeView(
    Notice, db.session,
    name='管理通知', endpoint='admin_notice'))


from .admin_user import admin_user
from .admin_topic import admin_topic
from .admin_follow import admin_follow
#from .admin_file import admin_file
admin_user(admin)
admin_topic(admin)
admin_follow(admin)
#admin_file(admin)