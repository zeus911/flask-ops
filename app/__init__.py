from flask import Flask
from flask.ext.admin import Admin
app=Flask(__name__)

admin = Admin(app,name='app')

import views
