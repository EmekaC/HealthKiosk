import mysql.connector, pymysql
import secrets

#Database specifications
dbhost = 'localhost'
dbuser = 'root'
dbpass = 'kiosk@DB1'
dbname = 'health-kiosk'

connection = f'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}'

#Flask app configurations
class Config:
    SQLALCHEMY_DATABASE_URI = connection
    JSON_SORT_KEYS = False
    SECRET_KEY = secrets.token_urlsafe(16)
    