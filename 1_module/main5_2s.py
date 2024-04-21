#main5_2s.py
#Большой обьект
users = {
    'user1':{'name':'Alex','age':23,'data':[5,6,3,3],'bio':'Some text','address':{'sity':'New York','street':'P'}},
    'user2':{'name':'Alex','age':23,'data':[5,6,3,3],'bio':'Some text','address':{'sity':'New York','street':'P'}},
    'user3':{'name':'Alex','age':23,'data':[5,6,3,3],'bio':'Some text','address':{'sity':'New York','street':'P'}},
    'user4':{'name':'Alex','age':23,'data':[5,6,3,3],'bio':'Some text','address':{'sity':'New York','street':'P'}},
}

print(users['user3']['name'])
print(users['user3']['address']['sity'])

# Самостоятельная работа
# Создайте кортеж colors с несколькими цветами (например, "красный", "зеленый", "синий").
# Создайте множество fruits_set с названиями фруктов (например, "яблоко", "банан", "апельсин").
# Создайте словарь ages с парами ключ-значение, где ключи - имена, а значения - возрасты
# (например, {'Анна': 25, 'Иван': 30, 'Мария': 22}).

# Выполните действия над созданными данными:
# Выведите в консоль элемент кортежа с индексом 1.
# Добавьте новый цвет в кортеж colors.
# Выведите в консоль множество fruits_set.
# Измените возраст 'Ивана' в словаре ages на 32.
# Выведите в консоль все имена из словаря ages.
# Удалите фрукт "апельсин" из множества fruits_set.
# Выведите в консоль все пары ключ-значение из словаря ages.


colors = ('красный','зеленый','синий')
fruits_set = {'яблоко','банан','апельсин'}
ages = {'Анна': 25, 'Иван': 30, 'Мария': 22}

print("Элемент кортежа с индексом 1:",colors[1])
#Добавьте новый цвет в кортеж colors с помощью конкатенации.

colors += ("желтый",)
print(colors)


print(fruits_set)

ages['Иван'] = 32
print(ages['Иван'])

print(list(ages.keys()))
print(list(ages.items()))

fruits_set.remove('апельсин')
print(fruits_set)

print(ages.items())
