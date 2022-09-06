from sqlite3 import *
from Parser_Rozetka import url, respons_soup, create_data


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


query_build_laptop_table = """
CREATE TABLE IF NOT EXISTS laptop (
    name TEXT,
    laptopID INTEGER PRIMARY KEY AUTOINCREMENT,
    pictureID INTEGER,
    price INTEGER,
    FOREIGN KEY (pictureID) REFERENCES picture (pictureID)
    );
"""

query_build_picture_table = """
CREATE TABLE IF NOT EXISTS picture (
    pictureID INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT
    );
    """


def execute_select(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        return res
    except Error as error:
        print(error)


def main():
    soup = respons_soup(url)
    data = create_data(soup)
    con = create_connect('BD_scrap_ROZETKA.sqlite')
    execute_build(con, query_build_picture_table)
    execute_build(con, query_build_laptop_table)

    for key, value in data.items():
        query_add_rows_laptop = f"""
        INSERT INTO
            laptop (name, pictureID, price)
        VALUES 
            ('{value['name']}', {key + 1}, {value['price']})
        """
        query_add_rows_picture = f"""
        INSERT INTO
            picture (link)
        VALUES 
            ('{value['picture']}')
        """
        execute_build(con, query_add_rows_laptop)
        execute_build(con, query_add_rows_picture)


if __name__ == '__main__':
    main()
