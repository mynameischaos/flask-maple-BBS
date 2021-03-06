
from flask import jsonify
from flask_maple import Auth
from flask_login import login_required, current_user
from flask_babelex import gettext as _
from maple import app, mail, db, redis_data
from maple.user.models import User, UserInfor, UserSetting, Role
from maple.main.models import set_email_send
from datetime import datetime, timedelta
from maple.main.models import RedisData


def check_time(func):
    def wrapper(*args, **kw):
        time = redis_data.hget('user:%s' % str(current_user.id),
                               'send_email_time')
        if time:
            try:
                time = time.split('.')[0]
                time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                if datetime.now() < time + timedelta(seconds=360):
                    return jsonify(judge=False, error="你获取的验证链接还未过期，请尽快验证")
            except TypeError:
                set_email_send(current_user.id)
            except ValueError:
                set_email_send(current_user.id)
        else:
            set_email_send(current_user.id)
        return func(*args, **kw)

    return wrapper


class Login(Auth):
    def register_models(self, form):
        user = self.User()
        user.username = form.username.data
        user.password = user.set_password(form.password.data)
        user.email = form.email.data
        userinfor = UserInfor()
        user.infor = userinfor
        usersetting = UserSetting()
        user.setting = usersetting
        role = Role.query.filter_by(name='unconfirmed').first()
        if role is None:
            role = Role()
            role.name = 'unconfirmed'
        user.roles.append(role)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    @login_required
    @check_time
    def confirm_email(self):
        if current_user.is_confirmed:
            return jsonify(
                judge=False,
                error=_('Your account has been confirmed,don\'t need again'))
        else:
            self.register_email(current_user.email)
            set_email_send(current_user.id)
            return jsonify(
                judge=True,
                error=_('An email has been sent to your.Please receive'))

    def confirm_models(self, user):
        user.is_confirmed = True
        self.db.session.commit()
        RedisData.set_user()


auth = Login(app, db=db, mail=mail, user_model=User, use_principal=True)
