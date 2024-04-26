#main3_1s.py
#условные операторы
if 5 == 5:
    print("some info")

# num = int(input("Enter number: "))
# if num == 5:
#     print("Number is five")
#     print("Должен быть одинаковый отступ")

# num = int(input("Enter number: ")) # ==,!=,<,>, <=,>=
# if num > 50:
#     print("Число больше за 50")

#     num2 = input("Enter word: ")
#     if num2 == "Word":
#         print("Должен быть одинаковый отступ")
# elif num == 10:
#     print("Number is 10")
# elif num == 11:
#     print("Number is 11")
# elif num == 12:
#     print("Number is 12")
# else:
#     print("Else")

#несколько условий
# num = int(input("Enter number: ")) # ==,!=,<,>, <=,>=
# hasBobCar = False

# if num > 50 and not hasBobCar:
#     print("Число больше за 50")

#     num2 = input("Enter word: ")
#     if num2 == "Word":
#         print("Должен быть одинаковый отступ")
# elif 5 < num < 10 or hasBobCar: #num < 10 and num >5
#     print("Number is 10")
# elif num == 11:
#     print("Number is 11")
# elif num == 12:
#     print("Number is 12")
# else:
#     print("Else")

#тернарный оператор
# number = float(input("Enter number: "))

# result = "Больше за 5.5" if number > 5.5 else "Меньше за 5.5"
# if number > 5.5:
#     result = "Больше за 5.5"
# else:
#     result = "Меньше за 5.5"

# print(result)

# Самостоятельная работа
# Запросите у пользователя ввод двух чисел.
# Запросите у пользователя выбор операции: сложение, вычитание, умножение или деление (+, -, *, /).
# В зависимости от того что ввел пользователь выполните выбранную операцию и выведите результат.
#Используйте условия для проверки введенных данных.


num1 = int(input("Введите 1е чило: "))
num2 = int(input("Введите 2е чило: "))
res = input("Введите операцию(+, -, *, /): ")

if res == "+":
    print(num1+num2)
elif res == "-":
    print(num1-num2)
elif res == "*":
    print(num1*num2)
elif res == "/":
    if num2 != 0:
        print(int(num1/num2))
    else:
        print("Ошибка:деление на ноль")
else:
    print("Вы ввели что-то не то")
