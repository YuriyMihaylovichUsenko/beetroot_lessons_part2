from peevee_create_my_players import *

city = [('New_York', 'USA', 6000),
    ('Californiya', 'USA', 4000),
    ('Nikolaiv', 'Ukraine', 500),
    ('Kyiv', 'Ukraine', 3000),
    ('Kremenchuk', 'Ukraine', 200),
    ('Cherkasy', 'Ukraine', 250)]

# for i in city:
#     city_dict = {'name': i[0], 'country': i[1], 'population': i[2]}
#     City.create(**city_dict)

team = [('bulls', 'Kremenchuk', 1),
    ('mankies', 'Cherkasy', 2),
    ('bk_Kyiv', 'Kyiv', 3)]

team_dicts = []
for i in team:
    city = City.select().where(City.name == i[1])
    dict_i = {'name': i[0], 'city_from': city, 'rating': i[2]}
    team_dicts.append(dict_i)

# Team.insert_many(team_dicts).execute()

players = [(23, 'Onil', 'bulls', 'New_York'),
    (8, 'Bryant', 'mankies', 'Californiya'),
    (12, 'Hizhnyak', 'bk_Kyiv', 'Nikolaiv')]

for i in players:
    city_from = City.select().where(City.name == i[3])
    team = Team.select().where(Team.name == i[2])
    dict_i = {'number': i[0], 'last_name': i[1], 'team': team, 'city_from': city_from}
    Players(**dict_i).save()

# for i in Team.select():
#     print(i.city_from.name)

# Players.delete().execute()