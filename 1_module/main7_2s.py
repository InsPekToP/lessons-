#main7_2s.py
#Функции на практике
#Создание словарей и нах. мин. эл-нт

# data1 = dict(x=5,y=8,z=-7,a=1,b=20) #альтернативный вид записи словаря data1 = {x:5...}

# minElement = 1000
# for k, v in data1.items():
#     if v < minElement:
#         minElement = v
# print(f"Min element: {minElement}")


# data2 = dict(x=5,y=8,z=7,a=-1,b=20)

# minElement = 1000
# for k, v in data2.items():
#     if v < minElement:
#         minElement = v
# print(f"Min element: {minElement}")


#Создаем ф-ию чтобы сократить эти 2 кода

def minimal(nums):
    minElement = 1000
    for v in nums.values():
        if v < minElement:
            minElement = v
    return minElement
    # print(f"Min element: {minElement}")

data1 = dict(x=5,y=8,z=-7,a=1,b=20)
data2 = dict(x=5,y=8,z=7,a=-1,b=20)

minimal(data1)
minimal(data2)

#Что такое return:

min1 = minimal(data1)
min2 = minimal(data2)

if min1 < min2:print(min1) # сейчас выводится ошибка,чтобы этого не было,нужно вернуть(return) minElement
#вместо вывода информации
else:print(min2)
