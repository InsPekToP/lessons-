#main4_1s.py
#Массивы данных.Работа со списками
data = [5,7.4,True,"Word",56,[0,15]]
data[2] = False
# print(data[5]) #list
# print(data[-1][-1])

#------------Функции-------------
data.append("info")

new_list = [5,7,3]
data.extend(new_list)

data.insert(1,0.567)

data.remove("info")

data.pop(0)

# new_list.sort()
# print(new_list)

data.reverse()
# data.clear()
# print(data)
# print(data.count(5))
# print(len(data))

#-----Индексы и срезы-----
print(data)
print(data[-1])
print(data[2:-2])
print(data[0:-1:2])

#-----Строки----

word = list('Some')
word[0] = 'T'
print(word)
print(word.count('m'))
print(len(word))

word2 = 'Hello'
print(word2.upper())
print(word2.lower())
print(word2.find('l'))


# Самостоятельная работа
# Создайте список fruits с несколькими названиями фруктов (например, "яблоко", "банан", "апельсин").
# Добавьте новый фрукт в список с помощью метода.
# Выведите в консоль длину списка.
# Используя специальный метод, вставьте фрукт "груша" в середину списка.
# Удалите фрукт "банан" из списка с помощью метода.
# Выведите в консоль индекс фрукта "апельсин" с помощью специального метода.
# Отсортируйте список.
# Выведите полученный отсортированный список в консоль.

fruits = ['яблоко','банан','апельсин']
fruits.append('киви')
fruits.insert(2,'груша')
fruits.remove('банан')


print('Индекс апельсина:',fruits.index('апельсин'))
print(fruits)
fruits.sort()

print(fruits)
print('Кол-во эл-тов в списке:',len(fruits))
