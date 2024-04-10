#2main11_1s.py
#Разработка программ на Python
#Конвектор валют Currency Converter
#Все осуществляется за счет библиотек в pypi.org.Также можно искать в гугле

#Создаем прогу для конвертации валют: pip install CurrencyConverter
#теперь можно импортировать

from currency_converter import CurrencyConverter #импортировали библиотеку

c = CurrencyConverter() #создали обьект на основе класса CurrencyConverter

res = c.convert(100, 'USD', 'EUR') #теперь сюда подставляем свои значения валюты
print(res)
