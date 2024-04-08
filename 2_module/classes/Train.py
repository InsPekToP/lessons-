from classes.Transport import Transport

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
