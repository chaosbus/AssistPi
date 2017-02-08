from flask import Blueprint
from . import views

admin = Blueprint('admin', __name__)

admin.add_url_rule('/', 'admin', views.index)
admin.add_url_rule('/login', 'login', views.login)

