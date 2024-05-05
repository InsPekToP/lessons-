#3main3_2s.py
# Самостоятельная работа
#
# Используя SQL-команду CREATE TABLE, создайте таблицу Book с полями:
#
# id (тип данных: INTEGER, автоинкремент),
# title (тип данных: VARCHAR(100)),
# author (тип данных: VARCHAR(50)),
# publication_year (тип данных: INTEGER),
# genre (тип данных: VARCHAR(30)).

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="book"
    #port = "8889" - для MAMP
)

cur = db.cursor()

#sql = "CREATE DATABASE IF NOT EXISTS book"

sql = '''CREATE TABLE IF NOT EXISTS Book(
        id int auto_increment primary key,
        title VARCHAR(100),
        author VARCHAR(50),
        publication_year INT,
        genre VARCHAR(30))'''


cur.execute(sql)


cur.close()
db.close()
