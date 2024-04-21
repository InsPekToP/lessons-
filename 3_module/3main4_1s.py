#3main4_1s.py
#Добавление данных в таблицы(SQL-команды)

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python-example"
    #port = "8889" - для MAMP
)

cur = db.cursor()

#sql = "INSERT INTO articles(title,intro,date) VALUES('Title','intro','20060-01-01')"
#ДОБАВИТЬ В таблицу articles,в такие поля
#(title,intro,date) значения прописываю после VALUES>
#поле id-первичный ключ,прописывается автоматически(AUTO-INCREMENT)
#VALUES('Title','intro','20060-01-01') - вводить не совсем корректно,т.к. пользователь может прописать
#('Title';DROP DATABASE) - и удалиться БД.Чтобы этого не было,нужны заглушки %s(будем подставлять строку)
sql = "INSERT INTO articles(title,intro,date) VALUES(%s,%s,%s)"
#теперь,чтобы поставить что-то,надо в .execute добавить кортеж со значениями
#если нужно добавить только 1 запись,все равно делаем кортеж('Вторая статья',)-и ставим запятую
#cur.execute(sql,('Вторая статья','Текст для второй статьи','2070-01-01'))

#Добавить набор из множесва записей.Надо создать список,и добавить в него кортеж
articles = [
    ('3 статья','Текст для 3 статьи','2100-01-01'),
    ('4 статья','Текст для 4 статьи','2100-01-01'),
    ('5 статья','Текст для 5 статьи','2100-01-01')
]

#cur.execute(sql,('Вторая статья','Текст для второй статьи','2070-01-01'))
#теперь вместо кортежа,мы подставляем список
cur.executemany(sql,articles) #будет выдавть ошибку т.к. надо ис-ть не execute,а .executemany

#cur.execute(sql)#>этого не хватит,нужен еще commit()-обновить
db.commit()





cur.close()
db.close()
