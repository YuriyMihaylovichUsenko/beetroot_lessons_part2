from sqlite3 import *
from pprint import pprint

def create_connect(path):
    try:
        con = connect(path)
        return con
    except Error as error:
        print(error)


def execute_build(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
    except Error as error:
        print(error)


query_build_team_table = """
CREATE TABLE IF NOT EXISTS team (
    name TEXT,
    city_from TEXT,
    rating INTEGER,
    FOREIGN KEY (city_from) REFERENCES cities (name)
    );
"""

query_build_players_table = """
CREATE TABLE IF NOT EXISTS players (
    number INTEGER,
    last_name TEXT,
    team TEXT,
    city_from TEXT,
    FOREIGN KEY (team) REFERENCES team (name),
    FOREIGN KEY (city_from) REFERENCES cities (name)
    );
    """

query_build_city_table = """
CREATE TABLE IF NOT EXISTS cities (
    name TEXT,
    country TEXT,
    population INTEGER
    );
    """

query_add_rows_team = """
INSERT INTO
    team (name, city_from, rating)
VALUES 
    ('bulls', 'Kremenchuk', 1),
    ('mankies', 'Cherkasy', 2),
    ('bk_Kyiv', 'Kyiv', 3);
"""

query_add_rows_players = """
INSERT INTO
    players (number, last_name, team, city_from)
VALUES 
    (23, 'Onil', 'bulls', 'New_York'),
    (8, 'Bryant', 'mankies', 'Californiya'),
    (12, 'Hizhnyak', 'bk_Kyiv', 'Nikolaiv');
"""

query_add_rows_cities = """
INSERT INTO
    cities (name, country, population)
VALUES 
    ('New_York', 'USA', 6000),
    ('Californiya', 'USA', 4000),
    ('Nikolaiv', 'Ukraine', 500),
    ('Kyiv', 'Ukraine', 3000),
    ('Kremenchuk', 'Ukraine', 200),
    ('Cherkasy', 'Ukraine', 250);
"""


def execute_select(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        return res
    except Error as error:
        print(error)


select_cities = """SELECT * FROM cities"""

select_all = """SELECT * 
FROM players 
INNER JOIN team on players.team = team.name
INNER JOIN cities on players.city_from = cities.name
"""
select_player_country = """
SELECT last_name, country FROM players
INNER JOIN cities on players.city_from = cities.name"""

#################################################################

update_row = """
UPDATE cities SET population = 3500 WHERE name = 'Kyiv'
"""

delete_row = """
DELETE FROM cities WHERE name = 'Californiya'"""

add_row = """
INSERT INTO
cities (name, country, population)
VALUES 
    ('Californiya', 'USA', 4000);"""

new_column = """
ALTER TABLE cities ADD COLUMN region TEXT"""

# Task 2
query_1 = """
SELECT first_name, last_name FROM employees"""


def main():
    con = create_connect('BD_Task1.sqlite')
    # execute_build(con, query_build_team_table)
    # execute_build(con, query_build_players_table)
    # execute_build(con, query_build_city_table)
    #
    # execute_build(con, query_add_rows_cities)
    # execute_build(con, query_add_rows_team)
    # execute_build(con, query_add_rows_players)

    # pprint(execute_select(con, select_cities))
    # pprint(execute_select(con, select_all))
    # pprint(execute_select(con, select_player_country))

    # execute_build(con, update_row)
    # execute_build(con, delete_row)
    # execute_build(con, add_row)
    execute_build(con, new_column)

    # Task 2
    con = create_connect('hr.db')
    pprint(execute_select(con, query_1))


if __name__ == '__main__':
    main()
