# HealthKiosk
IoT self service health kiosk

Structure of project:

kiosk_be: Contains the flask app
kiosk_fe: Contains react app
kiosk_sql: Contains sql scripts to create tables and dummy data for patients table

Required VSCode plugins:

1. ms-python.python
2. wyattferguson.jinja2-snippet-kit
3. ms-toolsai.jupyter


Project configs:

1. In .vscode -> settings.json: edit the python3 path that is relative to where the project is stored locally


Runing project:

1. Starting backend: cd to kiosk_fe and then run yarn run start-be
2. Starting frontend: cd to kiosk_fe and the run yarn run start


Required PIP packages:
- pip install Flask
- pip install PyMySQL
- pip install Flask-SQLAlchemy
- pip install mysql-connector-python
- pip install python-dotenv
- pip install flask-marshmallow
- pip install marshmallow-sqlalchemy
- pip install pylint
- pip install cryptography
- pip install PyJWT
- pip install datedelta
