#2main3_2s
#Наследование,инкапсуляция,полиморфизм
#Разбили класы по папкам,теперь импортируем их

from classes.Car import Car
from classes.Ship import Ship
from classes.Train import Train
#будет ошибка,связанная с файлом Transport(Car,Ship,Train нах в той же папке,что и Транспорт)
#нужно указывать полный путь

bmw = Car(200,2000,True)
train = Train(140,20000,False,5)
ship = Ship(50,5000,True)

train.get_info()

#Инкапсуляция - защита данных(в питоне прописать можно __)Можно не создавать поля и прога будет работать
#если в конструкторе прописаны эти поля

#Можем указывать какой тип данных будем получать(через двоеточие)
# def __init__(self, speed:int, weight:int, isWorking:bool,wagon_count:int) - выбивает подсказки


#def get_info(self)-> str: ---тоже подсказка какой тип будет возвращать(но работает криво)
