#2main2_1s
#ООП
#Программа без ис-ия ООП

# admin = {'name':'Alex','age':27,'allows':[2,4],'bio':'Some info'} #'allows'-список разрешений к 2му и 4ми блоку

# def printAllows(user): #создаем ф-ию printAllows,передаем ему пользователя user
#     print(user['allows']) #принтуем user,передаем ключ 'allows'

# printAllows(admin)

# user1 = {'name':'Bob','age':27,'bio':'Some info'} 
# user2 = {'name':'Bob','age':27,'bio':'Some info'} 
# user3 = {'name':'Bob','age':27,'bio':'Some info'} 

# #На данный момент у этих 4х польз-ей нет общего ф-ла.Если их будет не 4,а 1000,то будет сложно что -либо
# #с ними сделать.Для этого существуют классы



#Классы в ООП

class User: #создали класс,закинули пар-ры(name,email и т.д.) и присвоили None
    name = None
    email = None
    login = None
    age = None

    #Конструкторы
    # def __init__(self): #контруктор самого класса(ничего не принимает и не передает?)
    #     pass
    def __init__(self,name,email,login='None',age=20): #теперь принимае пар-ры.Также можем устанавливать
        #пар-ры,а потом переопределять(login='None,age=20)
        # self.name = name
        # self.email = email
        # self.login = login
        # self.age = age
        #можно еще больше упростить
        self.set_info(name,email,login,age) #в ф-ии __init__ обр-мся  к ф-ии set_info
        self.get_info() #в ф-ии __init__ обр-мся  к ф-ии get_info

#добавляем новую ф-ию(метод)
    def set_info(self,name,email,login,age): #ф-ия,кот будет что-то устанавливать,self писать обяз-но
        #name = name #к тому знач. name кот.есть в классе я подставляю то знач. кот. принимаем от
        #поль-ля в ф-ии.Но это не понятно,лучше указать self
        self.name = name #self.name - внутри class,и в качестве знач. переменной устанавливаю name
        #внутри ф-ии
        self.email = email
        self.login = login
        self.age = age

    def get_info(self):
        print(f"User: {self.name}, login: {self.login}, email: {self.email}, Age: {self.age}")


# admin = User() #на основе класса User создаем новых поль-ей(admin,Bob,Alex)
# bob = User()
# alex = User()

#Благодаря конструктору __init__ теперь можно при вызове admin = User(),могу сразу передавать туда пар-ры
admin = User('Bob','bob@mail.com','Modest',26)
bob = User('Alex','alex@mail.com') #тогда сдесь будет login по умолчанию None,а age = 20
alex = User('Admin','bob@mail.com',age=27) #а сдесь переопределили age=27

# bob.set_info('Bob','bob@mail.com','Modest',26) #уст-ли пар-ры через ф-ию set_info
# alex.set_info('Alex','alex@mail.com','Modest',26)
# admin.set_info('Admin','bob@mail.com','Modest',26)


#теперь и это можем закомнтить,т.к. в конструкторе __init__ все прописали
# bob.get_info() #выводим ин-ию через ф-ию get_info
# alex.get_info()
# admin.get_info()





#{Это все тоже можем удалить т.к. прописали ф-ию get_info
# admin.login = 'Admin' #обращаемся к полю,и устанавливаем туда значения
# # bob.login = 'Bob' #это теперь можем удалить,т.к. уснановили через ф-ия set_info
# alex.login = 'Alex'

# print(admin.login)
# print(alex.login)
# print(bob.email)
#}
