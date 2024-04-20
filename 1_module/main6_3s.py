#main6_3s.py
#Работа с пользователем
# user_data = []
# number = int(input("Введите число: "))

# for i in range(number):
#     el = input("Enter value: ")

#     user_data.append(el)

# print(user_data)


#Перебор списка,нах. максимального результата
user_data = []
number = int(input("Введите число: "))

for i in range(number):
    el = int(input("Enter value: "))

    user_data.append(el)

print(user_data)

maxElement = 0
for i in user_data:
    if i > maxElement:
        maxElement = i
print("Max Element", maxElement)
