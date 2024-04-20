#main6_4s.py
#Функции для строк

hobbies = 'skate,football,paiting'
listHobbies = hobbies.split(',')
newListHobbies = []

for i in listHobbies:
    newListHobbies.append(i.capitalize())
res = ",".join(newListHobbies)
print(res)

# Самостоятельная работа
# Создайте список marks с оценками студентов – [85, 90, 78, 95, 88].
# Используя цикл for, выведите каждую оценку из списка в консоль,--
# --добавив сообщение "Оценка:" перед каждой оценкой.
# Используя цикл for, найдите и выведите среднюю оценку.
# Используя цикл while, увеличьте каждую оценку в списке на 5 баллов.
# Выведите обновленные оценки с использованием цикла for.

marks = [85, 90, 78, 95, 88]

for i in marks:
    print("Оценка:",i)

# Используя цикл for, найдите и выведите среднюю оценку.
average_mark = sum(marks) / len(marks)
print(f'Средняя оценка: {average_mark}')

# Используя цикл while, увеличьте каждую оценку в списке на 5 баллов.
index = 0
while index < len(marks):
    marks[index] += 5
    index += 1
print(marks)

# Выведите обновленные оценки с использованием цикла for.
for i in marks:
    print(f"Обновленная оценка:{i}")
