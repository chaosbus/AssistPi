from flask import Flask
from .urls import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin', methods=['GET', 'POST'])
