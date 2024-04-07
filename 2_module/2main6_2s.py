#2main6_2s.py
# Самостоятельная работа
# Импортируйте модуль threading.
# Создайте функцию print_numbers(), которая будет выводить числа от 1 до 5 с интервалом 1 секунда.
# Создайте объект thread для выполнения функции print_numbers.
# Запустите поток и дайте ему время выполниться.
# В основном потоке также выведите строку "Главный поток завершил работу".


import time
import threading

def print_numbers():
    for i in range(1,6):
        print(f'Число: {i}')
        time.sleep(1)

thread = threading.Thread(target=print_numbers)

thread.start()

print('Главный поток завершил работу')
