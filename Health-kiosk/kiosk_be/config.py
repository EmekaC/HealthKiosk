import mysql.connector, pymysql
import secrets

dbhost = 'localhost'
dbuser = 'root'
dbpass = 'password12345%'
dbname = 'health-kiosk'

connection = f'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}'

class Config:
    SQLALCHEMY_DATABASE_URI = connection
    JSON_SORT_KEYS = False
    SECRET_KEY = secrets.token_hex(16)
    