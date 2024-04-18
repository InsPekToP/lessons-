#main7_1s
#Функции в Python
# def test():
#     #pass
#     print("Some")

#Передача пар-ов

# def test(word):
#     print(word,"!", sep = "")

# test("Some")

# some = "Word"
# test(some)
# test(6.6)

#Математическая ф-ия

# def test(word):
#     print(word,"!", sep = "")

# def add(x,y):
#     res = x + y
#     test(res)

# add(5,7)
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# add(num1,num2)

#Возвращение данных, return

# def test(word):
#     print(word,"!", sep = "")

# def add(x,y):
#     res = x + y
#     test(res)

#     return res

# # add(5,7)
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# res = add(num1,num2)
# print(res)


#Значение по умолчанию

# def test(word):
#     print(word,"!", sep = "")

# def add(x=5,y=5,additional=0):
#     res = x + y + additional
#     test(res)

#     return res

# add(5,7)
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# res = add(10,15,2)
# print(res)

#Неизвестное кол-во параметров

def test(word):
    print(word,"!", sep = "")

def add(x=5,y=5,additional=0):
    res = x + y + additional
    test(res)

    return res

# def mult(x,y,*args):
#     print(x,y,args)

# mult(6,8,True,"Some")

#Можно также без x и y
def mult(*args):
    for i in args:
        i *=2
        print(f"Element:{i} ")


mult(6,8,True,"Some")

#Получение словаря

def test(word):
    print(word,"!", sep = "")

def add(x=5,y=5,additional=0):
    res = x + y + additional
    test(res)

    return res

def mult(**kargs): #чтобы сделать словарь
    for key,value in kargs.items(): #перебираем ключ и значение в .items(во всем)
        
        print(f"Element:{value}, key:{key} ")


mult(x=6,y=8,additional = 10, some = "Word")
