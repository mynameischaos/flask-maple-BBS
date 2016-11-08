### Activity for Tsinghua

#### Environments

* Pycharm

* Python, Flask, Flask-maple

* Redis, PostgreSQL


#### Features

* Register & login & forget password
* Board and tags
* Collect
* Like replies
* Follow tags,users,topics
* Privacy setting
* Choice markdown to ask
* Tags rss
* Avatar
* Topic vote

#### Installation

##### Pull the code

```
git clone https://github.com/mynameischaos/flask-maple-BBS.git

```

##### Install Python

* Install Python3.3 or a later version

##### Install necessary package

* sudo pip install -r requirements.txt

##### Install flask-maple

```
git clone https://github.com/honmaple/flask-maple
cd flask-maple
python setup.py install
```
##### Install Redis

Use default settings, and run redis server:

```
wget http://download.redis.io/releases/redis-3.2.5.tar.gz
tar -zvxf redis-3.2.5.tar.gz
cd redis-3.2.5.tar.gz
make && make install
```

run redis server:

```
redis-server
```

##### Install PostgreSQL

Install and create user(postgres) and password(zhonghuasong)

Create database 'db'

Run PostgreSQL server:

```
pg_ctl - D / usr / local / var / postgres - l / usr / local / var / postgres / server.log start
```

#### Init database

##### Comment befor init database

Place of file : maple/topic/forms.py

```
#category = SelectField(
#    _('Category:'),
#    choices=[(b.id, b.board + '   --' + b.parent_board)
#             for b in Board.query.all()],
#    coerce=int)
```

##### Init sql

```
python3 manager.py db init
python3 manager.py db migrate -m "first migrate"
python3 manager.py db upgrade
```

Ok, please uncomment the content of maple/topic/forms.py

##### Create admin account

```
python3 manager.py create_user
```

##### Run server and visit index page

```
forums.localhost:5000
```

##### Login and visit admin page

Use the admin account to login in and visit.

```
forums.localhost:5000/admin
```





