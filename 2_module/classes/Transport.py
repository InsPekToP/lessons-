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
