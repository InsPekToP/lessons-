#2main1_1s
#Модули ООП в Python

# import math,time,platform #можно в одну строку,через зяпятую,но лучше с разных

import math
# import time
from time import sleep #из модуля time импортируем ф-ию sleep
import platform as pl #дали псевдоним

#создаем файл my_module.py
import my_module #импортируем созданый модуль(расширение прописывать не надо),
#если перекинули в папку,надо указать путь(data.my_module)
#сразу выводится Hello.Т.к. код сразу выполняется,чтобы Hello не выводился при импорте.
#Нужно в my_module прописать if __name__ == "__main__":print("Hello") ---если данный модуль
#будет запускаться как отдельный файл,то в нем будет срабатывать кусочек кода print("Hello").
#Но если импортируем,то не будет срабатывать.То есть,если прописать в терминале python my_module.py 
#выведется Hello

my_module.printSome(my_module.some) #Обратились к модулю,и к printSome(),в скобочках опять обратились
#к my_module и к переменной .some.
my_module.printSome(my_module.summa(5,7,3,8)) #тоже самое,но теперь обратились к ф-ии summa в файле my_module

#import my_module as m #добавили псевдоним(можно добавлять ко всем модулям)

from my_module import printSome,summa #им-ли из my_module printSome,summa.Теперь мне не нужно делать псевдоним,
#или об-тся к my_module
my_module.printSome(my_module.summa(5,7,3,8)) #это до
printSome(summa(5,7,3,8)) #это после





print(pl.platform()) #узнаем инфу о платформе
print(pl.system()) #о винде
print(pl.release()) #версии винды


# time.sleep(2) #усыпляем прогу на 2 сек.
#from time import sleep
#sleep(2) #теперь обращаемся только к sleep(т.к. был им-ан только этот модуль)



res=math.pow(2,3) #возводит 2 в степень 3
print(int(res))
print(math.pi)
print(math.e)

res2 = math.pow(math.pi,3) #возводим ПИ в 3ю степень
print(math.ceil(res2)) #.ceil округляет к большему
print(math.floor(res2)) #.floor округляет к меньшему
print(round(res2)) #round - не вызывается из math,округляет к ближайшему числу




