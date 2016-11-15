
from maple import db
from sqlalchemy import event
from .models import User, Role

__all__ = ['add_role_after_confirm', 'add_role_after_super']


@event.listens_for(User.is_confirmed, 'set')
def add_role_after_confirm(target, value, oldvalue, initiator):
    role = Role.query.filter_by(name='confirmed').first()
    if not role:
        role = Role()
        role.name = 'confirmed'
        role.description = 'confirmed'
        db.session.add(role)
        db.session.commit()
    if value and role not in target.roles:
        target.roles.append(role)
    if not value and role in target.roles:
        target.roles.remove(role)


@event.listens_for(User.is_superuser, 'set')
def add_role_after_super(target, value, oldvalue, initiator):
    role = Role.query.filter_by(name='super').first()
    if not role:
        role = Role()
        role.name = 'super'
        role.description = 'super'
        db.session.add(role)
        db.session.commit()
    if value and role not in target.roles:
        target.roles.append(role)
    if not value and role in target.roles:
        target.roles.remove(role)
