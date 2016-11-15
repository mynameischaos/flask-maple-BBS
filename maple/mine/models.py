
from maple import db
from maple.tag.models import Tags
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import (generate_password_hash, check_password_hash)
from sqlalchemy import event


class Follow(db.Model):
    __tablename__ = 'follows'
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    following_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    following_tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    following_collect_id = db.Column(db.Integer, db.ForeignKey('collects.id'))
    followinf_topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
