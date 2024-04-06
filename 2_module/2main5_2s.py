#2main5_2s.py
#Enum - перечисления(подсказки)
# Самостоятельная работа
# Импортируйте модуль Enum из библиотеки enum.
# Создайте перечисление с названием DaysOfWeek, представляющее дни недели.
# В DaysOfWeek добавьте элементы: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.
# Выведите в консоль все значения из перечисления DaysOfWeek. Используйте для этого цикл.

from enum import Enum

class DaysOfWeek(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7




for day in DaysOfWeek:
    print(day)
