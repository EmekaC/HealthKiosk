from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from be.config import Config

#Main flask app

db = SQLAlchemy()
ma = Marshmallow()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)

#import views
from be.views.patient_view import patients_view
from be.views.login_view import login_view
from be.views.results_view import results_view
from be.views.nok_view import next_of_ken_view
from be.views.doctors_view import doctor_view

#register view blueprints
app.register_blueprint(patients_view)
app.register_blueprint(login_view)
app.register_blueprint(results_view)
app.register_blueprint(next_of_ken_view)
app.register_blueprint(doctor_view)
    

