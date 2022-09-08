from HomeWork_34 import create_connect, execute_select
from pprint import pprint

connection = create_connect('northwind.db')

# Вибрати усіх клієнтів
customers = """
"""
# for item in execute_select(connection, customers):
#     print(item)

# Вибрати усіх клієнтів, але тільки ім'я та місто
customers_name_city = """
"""
# for item in execute_select(connection, customers_name_city):
#     print(item)

# Вибрати усі міста звідки клієнти але без повтореннь
customers_unique_cities = """
"""
# for item in execute_select(connection, customers_unique_cities):
#     print(item)

# Вибрати усі міста та країни звідки клієнти але без повтореннь
customers_unique_cities_countries = """
"""
# for item in execute_select(connection, customers_unique_cities_countries):
#     print(item)

# Порахувати кількість замовників
customers_count = """
"""
# for item in execute_select(connection, customers_count):
#     print(item)

# Порахувати кількість унікальних країн з яких наші клієнти
customer_countries_count = """
"""
# for item in execute_select(connection, customer_countries_count):
#     print(item)

###############################################################################
# Вибрати усі замовлення з країн Франція, Австрія, Іспанія
orders_from_countries = """
"""
# for item in execute_select(connection, orders_from_countries):
#     print(item)

# Вибрати усі замовлення та відсортувати по даті замовлення по зменшенню та по
# даті відгрузки по зростанню
orders_sorted = """
"""
# for item in execute_select(connection, orders_sorted):
#     print(item)

# Вибрати мінімальну ціну серед продуктів яких не менше 30 одиниць у продажу
min_product_price = """
"""
# for item in execute_select(connection, min_product_price):
#     print(item)

# Знайти середню кількість днів, що йде на формування замовлень з США
average_usa_order_days = """
"""
# for item in execute_select(connection, average_usa_order_days):
#     print(item)

# Порахувати загальну суму на яку маємо товарів
products_sum = """
"""
# for item in execute_select(connection, products_sum):
#     print(item)

# Вибрати всі замовлення у яких країна починається з U
orders_from_U = """
"""
# for item in execute_select(connection, orders_from_U):
#     print(item)

# Вибрати замовлення, що мають бути відвантажені в країну, що починається з N
# відсортувати по вазі по зменшенню та вивести тільки перші 10 результатів
orders_from_N = """
"""
# for item in execute_select(connection, orders_from_N):
#     print(item)

# Знайти замовників у яких ми не маємо телефонів
customers_no_phone = """
"""
# for item in execute_select(connection, customers_no_phone):
#     print(item)

# Порахувати клієнтів, що мають телефон
customers_with_phone_count = """
"""
# for item in execute_select(connection, customers_with_phone_count):
#     print(item)

# Порахувати постачальників з кожної країни, відсортувати по кількості
# по зменшенню
suppliers_from_country_count = """
"""
# for item in execute_select(connection, suppliers_from_country_count):
#     print(item)

# Порахувати сумарну вагу замовлень в яких відомий регіон
# потім відфільтрувати тільки ті в яких вага більше 2750 та відсортувати
# по зменшенню
orders_sum_freight = """
"""
# for item in execute_select(connection, orders_sum_freight):
#     print(item)

# Вибрати унікальні країни замовників та постачальників та відсортувати
# по збільшенню
unique_suppliers_customers_countries = """
"""
# Показати різницю з UNION ALL
# for item in execute_select(connection, unique_suppliers_customers_countries):
#     print(item)

# Вибрати країни з яких замовники, постачальники та робітники
countries_employees_suppliers_customers = """
"""
# for item in execute_select(connection, countries_employees_suppliers_customers):
#     print(item)

# Вибрати країни з яких замовники, постачальники але не робітники
countries_not_employees_suppliers_customers = """
"""
# for item in execute_select(connection, countries_not_employees_suppliers_customers):
#     print(item)

###############################################################################
# Знайти замовників та співробітників, що обслуговують їх замовлення
# вони мають бути з Лондона і ті і ті, а доставка має йти компанією
# доставки Speedy Express
# вивести ім'я прізвище робітника та компанії замовника
customer_company_employee = """
"""
# for item in execute_select(connection, customer_company_employee):
#     print(item)

# Знайти замовників, що не зробили жодного замовлення
customers_with_no_orders = """
"""
# Показати що буде просто з JOIN
# for item in execute_select(connection, customers_with_no_orders):
#     print(item)

###############################################################################
# Subqueries
# Вивести усі унікальні товари яких замовлено рівно 10 одиниць
products_ordered_ten = """
"""
# for item in execute_select(connection, products_ordered_ten):
#     print(item)

products_ordered_ten_join = """
"""
for item in execute_select(connection, products_ordered_ten_join):
    print(item)
