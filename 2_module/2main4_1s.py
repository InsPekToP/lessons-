#2main4_1s
#Магические методы
# print(dir(int)) # позволяет вывести все магические методы,кот. прис-ют у класса или метода

#__add__ вызывается когда пишем +

# num = 10
# print(num + 5)
#тоже самое,но через магические методы
#print(num.__add__(7))

#__pow__ возведение в квадрат
#__abs__ значение числа по модулю
#Если создадим свой класс,можем переписать маг методы

class Some:

    name = "John" #ввели для маг.метода __str__
    number = 20 #ввели для __ge__


    def __add__(self,str): # переписываем метод
        print("Some " + str)
#теперь 2 метода,кот. срабатывают при создании самого обьекта

    # def __new__(self): #срабатывает при создании обьекта #служит для переписания самого обьекта
    #     # print("New object")
    #     self.__add__(self,"new") #прописали(хУЙ ЗНАЕТ ЗАЧЕМ)
    #     self.__init__(self) #ТОЖЕ НЕ ПОНЯТНО НАХЕРА ПРОПИСАЛИ
#теперь получается ошибка,т.к. переписали метод __new__(надо закоментить obj.__add__(" new"),obj + " new")


    def __init__(self): #срабатывает при инициализации обьекта(после его создания)
        print("Init started")

    def __str__(self): #вызывается когда пытаемся вывести обьект на экран print(obj)
#можем переписать этот метод
          return "Name " + self.name #позволяет писать что конкретно будет выводится(НИХУЯ БЛЯТЬ НЕ ПОНИМАЮ)

    def __ge__(self, x): # >=
        if(self.number >= x):
            return True
        else:
            return False
        
    #def __lt__ ---< -меньше
    #def __gt__ ---> -больше
    #def __eg__ ---== - равенство
    #def __lt__ ---!= - не равентсво
    #def __le__ ---<= - меньше или равно

    def __del__(self): #работает при удалении самого обьекта
        print("Delete object")



obj = Some()
#Если прописать +,вызовется маг метод __add__
obj + " new"
#или так
# obj.__add__(" new")

print(obj)
print(obj>=50) #делая такую конструкцию,мы обращаемся к маг.методу __ge__



print(dir(obj)) #смотрим какие изначально есть маг методы