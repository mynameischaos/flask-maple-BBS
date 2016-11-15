
from flask import Blueprint, render_template, send_from_directory
from os import path as ph

site = Blueprint('docs',
                 __name__,
                 template_folder='templates',
                 static_folder='static')


@site.route('/')
def docs():
    return render_template('docs/doc_list.html')


@site.route('/flask-maple/<path:path>')
def flask_maple(path):
    return send_from_directory(
        ph.join(site.static_folder, 'flask-maple'), path)


@site.route('/flask-avatar/<path:path>')
def flask_avatar(path):
    return send_from_directory(
        ph.join(site.static_folder, 'flask-avatar'), path)
