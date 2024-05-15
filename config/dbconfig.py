from urllib.parse import quote_plus as urlquote

account = 'starwa1kin_1'
password = '@StarWa1kin'
database = "flask_app"

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{account}:{urlquote(password)}@starwa1kin.mysql.rds.aliyuncs.com:3306/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
