#main6_2s.py
#Практическая часть
#Список
# data = [5,7,True,"Word",[6,8]]

# for el in data:
#     print(f"Element:{el}")

#Кортеж
# data = (5,7,True,"Word",[6,8])

# for el in data:
#     print(f"Element:{el}")

#Множества
# data = {5,7,True,"Word"}

# for el in data:
#     print(f"Element:{el}")

#Словари
data = {5,7,True,"Word"}
user  = {'name': 'John','age': 25,(6,7): True,False:7.7}

# for el in user.values():
#     print(f"Element:{el}")

# for el in user.keys():
#     print(f"Element:{el}")

# for el in user.items():
#     print(f"Element:{el[0]}")

# for el in user.items():
#     print(f"Element:{el[1]}")

for key,el in user.items():
    print(f"Key:{key}.Element:{el}")
