from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from salt import  client

app=Flask(__name__)

Bootstrap(app)

app.config.from_object('config')

db = SQLAlchemy(app)

saltclient = client.LocalClient()

import views,models
