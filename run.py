# *************************************************************************
#   Copyright  2015 JiangLin. All rights reserved.
#   File Name: run.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2016-02-07 09:12:47
# *************************************************************************
# !/usr/bin/env python
# -*- coding=UTF-8 -*-
from maple import app
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
