from peewee import *

db = MySQLDatabase(
    'db_konro', 
    user='root', 
    password='',
    host='localhost', 
    port=3306 )

class BaseModel(Model):
    class Meta:
        database = db