#main5_1s.py
# Разновидности списков:кортежи,множества,словари
#кортежи(tuple)
data = (5,4,6,True,[6,8])

# data[2] = 56 - нельзя изменять кортежи
print(data.count(5))
print(data[0:2])
print(data[::-3])
print(len(data))

word = list('Some')
print(word)

word = tuple('Some')
print(word)

#Множества (set)
data2 = {5,6,8,5}
data2.add(78)
data2.remove(6)
data2.pop()
data2.clear()

word2 = set('Hello')
word3 = frozenset('Hello') #замороженное множество

print(data2)
print(word2)
print(word3)
# print(data2[0]) - не можем обратиться по индексу


#Словари(dict)

user = {'name':'Alex','age': 15, 5:6, True : 5,(5,6): 5 }

user[(5,6)] = 6
user.popitem() #удаляет последний эл-нт
user.pop('age') # удаляет эл-нт по ключу
#user.clear() #очищает словарь


print(user['name'])
#print(user['age'])
print(user[5])
#print(user[(5,6)])
