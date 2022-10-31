import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "pet_shop",
    user = "thunyaung",
    password = "")

cursor = connection.cursor()

create_user_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, usertype text)"
cursor.execute(create_user_table)

create_items_table = "CREATE TABLE IF NOT EXISTS pets (id INTEGER PRIMARY KEY, pet_name text, price real, info text, user_id integer, category_id integer)"
cursor.execute(create_items_table)

create_category_table = "CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, category_name text)"
cursor.execute(create_category_table)

connection.commit()
cursor.close()

connection.close()

