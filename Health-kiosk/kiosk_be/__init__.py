from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from kiosk_be.config import Config

db = SQLAlchemy()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
@app.route('/')
def hello():
    return "hello world"
    
'''
import views
from test.views.patients import patients
register view blueprints
app.register_blueprint(patients)
'''
