#2main3_1s
#Наследование,инкапсуляция,полиморфизм
#Наследование
class Transport:
    # speed = None
    # weight = None
    # isWorking = None

    def __init__(self,speed,weight,isWorking):
        self.speed = speed
        self.weight = weight
        self.isWorking = isWorking
        self.get_info() #запускаем ф-ию вывода на экран

    def get_info(self):
        work = "Работает" if self.isWorking else "Не работает"
        print(f"Speed: {self.speed}, weight: {self.weight}, Is Working: {work}")

#чтобы добавить инфо в бмв,надо вписать ее в класс Transport(не удобно)Лучше создать классы,кот будут наследовать
#все от Transport
        
class Car(Transport): #создали класс Car на основе класса Transport
    pass
class Train(Transport): #мы можем дописать новые х-ки лишь для того вида транспотра кот.нужен
    wagon_count = None
    def __init__(self, speed, weight, isWorking,wagon_count): #создали ф-ию,кот. принимает теже пар-ры,что и осн.
        #ф-ия и добавили wagon_count
        # self.speed = speed
        # self.weight = weight
        # self.isWorking = isWorking #можно так записать,но логичнее так:
        super(Train,self).__init__(speed,weight,isWorking) #обратились к гл. класу(super) и дали ему теже пар-ры
        #и добавили wagon_count
        # self.get_info()
        self.wagon_count = wagon_count #добавили и сюда wagon_count
#Полиморфизм - в классах наследниках можем переписывать базовый ф-ал главного класса
    def get_info(self):
        super().get_info()
        print(f"Wagon count:{self.wagon_count}") #теперь в методе get_info будет высвечиваться и кол-во вагонов

        
class Ship(Transport):
    pass    


# bmw = Transport(200,2000,True) #создаем обьект на основе класса Transport и передаем ему 3 пар-ра
# train = Transport(140,20000,False)
# ship = Transport(50,5000,True)

#теперь можем переопределить создание классов
bmw = Car(200,2000,True)
train = Train(140,20000,False,5)
ship = Ship(50,5000,True)

train.get_info()

#Инкапсуляция - защита данных(в питоне прописать можно __)Можно не создавать поля и прога будет работать
#если в конструкторе прописаны эти поля
