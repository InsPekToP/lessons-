#3main2_1s.py
#Работа с MySQL(Подключение)
#Надо скачать прогу для локального сервера MAMP https://www.mamp.info/en/windows/
#не получилось запустить,пользуюсь XAMP

#перешли c VSCode

#Нужно установить MySQL pip install mysql-connector-python(https://pypi.org/project/mysql-connector-python/)
#проверить подключился ли MySQL:

import mysql.connector #если тут подсвечивает ошибку
#pip install mysql-connector-python-rf - если библиотека mysql не работает

#подключение к локальному серверу:

mydb = mysql.connector.connect( #connect() - ф-я позволяет подключится к локальному серверу.
#нужно указать несколько значений:
    host="localhost", #url-алресс сервера к кот. хотим подключится
    user="root", #логин-MAMP(root).Другие - mysql.У меня root
    password="" #пароль-MAMP(root).Другие-либо пусто,либо mysql.У меня пусто.
#можем скопировать с основной странички localhost/MAMP.Но у нас XAMP поэтому:
    #port = "8889" - для MAMP
)

print(mydb)
