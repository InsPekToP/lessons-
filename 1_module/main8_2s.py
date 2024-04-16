#main8_2s
#Самостоятельная работа
# Создайте простую функцию multiply, принимающую два аргумента и возвращающую их умножение.
# Создайте декоратор double_result, который удваивает результат функции.
# Примените декоратор к функции multiply с использованием синтаксиса @.
# Вызовите функцию multiply и выведите результат в консоль.


def double_result(func):
    def wrapper(x,y):
        result = func(x,y)
        return result *2
    return wrapper


@double_result
def multiply(x,y):
    return x*y

result = multiply(5,3)
print(f'Результат умножения с удвоением: {result}')
