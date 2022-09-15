from peewee import *
from pprint import pprint

db = SqliteDatabase("c:\pythonProject\\my_players.db")

class BaseModel(Model):
    class Meta:
        database = db


class City(BaseModel):
    name = CharField()
    country = CharField()
    population = IntegerField()


class Team(BaseModel):
    name = CharField()
    city_from = ForeignKeyField(City)
    rating = IntegerField()


class Players(BaseModel):
    number = IntegerField()
    last_name = CharField()
    team = ForeignKeyField(Team)
    city_from = ForeignKeyField(City)


if __name__ == '__main__':
    db.create_tables([City, Team, Players])
