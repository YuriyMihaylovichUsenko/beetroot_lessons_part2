import sqlite3

query = """
select * from product join image i on product.id = i.product_id
join price
where name == 'Ноутбук Lenovo V14 G2 ITL (Intel i3-1115G4/8/128F/int/W10Pro) Black'
"""

con = sqlite3.connect('rozetka.db')
curs = con.cursor()
curs.execute(query)
res = curs.fetchall()

for i in res:
    print(i)