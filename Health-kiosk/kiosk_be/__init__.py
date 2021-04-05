from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from kiosk_be.config import Config

db = SQLAlchemy()
ma = Marshmallow()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

#import views
from kiosk_be.views.patient_view import patients_view
from kiosk_be.views.login_view import login_view
#register view blueprints
app.register_blueprint(patients_view)
app.register_blueprint(login_view)
