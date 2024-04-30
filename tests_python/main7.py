#main7.py
# i = 5
# while i <=15:
#     print(i)
#     i += 2

# i = 5
# isHasCar = True
# while isHasCar:
#     print(i)
#     i += 2 #бесконечный цикл

isHasCar = True

while isHasCar:
    if input("Enter date: ") == "Stop":
        isHasCar = False
