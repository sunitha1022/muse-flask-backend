# import * means import everything from peewee
from peewee import *
import datetime
# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_dog_app', host='localhost', port=5432)
# setup a Song model with a created_at field and at least three properties of CharField(): title, artist, album


class Song(Model):
    title = CharField()
    artist = CharField()
    album = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Song], safe=True)
    print("TABLES Created")
    DATABASE.close()
