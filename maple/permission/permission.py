
from flask_principal import Permission, RoleNeed
from collections import namedtuple
from functools import partial

TopicNeed = namedtuple('topic', ['method', 'value'])
EditTopicNeed = partial(TopicNeed, 'edit')

ReplyNeed = namedtuple('reply', ['method', 'value'])
EditReplyNeed = partial(TopicNeed, 'edit')


CollectNeed = namedtuple('collect', ['method', 'value'])
GetCollect = partial(CollectNeed, 'get')
PostCollect = partial(CollectNeed, 'post')
PutCollect = partial(CollectNeed, 'put')
DeleteCollect = partial(CollectNeed, 'delete')

LikeNeed = namedtuple('like', ['method', 'value'])
GetLike = partial(CollectNeed, 'get')


class EditTopicPermission(Permission):
    def __init__(self, topicId):
        need = EditTopicNeed(topicId)
        super(EditTopicPermission, self).__init__(need)


class EditReplyPermission(Permission):
    def __init__(self, replyId):
        need = EditReplyNeed(replyId)
        super(EditReplyPermission, self).__init__(need)


super_permission = Permission(RoleNeed('super'))
