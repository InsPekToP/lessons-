#3main5_1s.py
#5 ВЫБОРКА УДАЛЕНИЕ И ОБНОВЛЕНИЕ БД

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python-example"
    #port = "8889" - для MAMP
)
cur = db.cursor()

#Основное содержимое
#Выбирать различные записи

#sql = "SELECT * FROM articles" #ВЫБИРАЕМ все(*) поля ИЗ таблицы articles
sql = "SELECT id,title,intro FROM articles WHERE intro LIKE %s OR id>%s ORDER BY id DESC LIMIT 1 OFFSET 1"
#выбираем 1 поле title + intro,ГДЕ(if else-но в SQL) id = 3>теперь ошибки нет,т.к. курсор принимает только 1 знач.
#также можем проверять на >=,<=  и неравество <>
#Также можно по другим полям искать WHERE title<>'Title'
#Также можно сделать выборку на схожесть intro LIKE 'второй'(% - не важно что было до и после)
#NOT LIKE - все поля без '%второй%'
#AND OR - также можно прописывать в команде
#intro LIKE '%второй%' id>3 - можно подставлять на прямую,а можно попозже LIKE %s OR id>%s
#ORDER BY - сортировка по полю(может прописываться без WHERE)
#DESC - в обратном порядке
#LIMIT- лимитирование записей
#OFFSET - пропуск записей
cur.execute(sql,('%второй%',3))

res = cur.fetchall() #чтобы выбрать все знач. ис-ем ф-ию .fetchall()
#res = cur.fetchone() #ф-я выводит 1 запись.Но выводится ошибка из-за курсора(содержал больше инфы чем надо)>
#print(res)
for el in res: #перебираем и выводим на экран
    print(el)


cur.close()
db.close()
