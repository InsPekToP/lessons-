#main10_2s
#Обработчик исключений
# num = 10/0
# sum()
#print(some)

# try:
#     num = int(input("Enter num: "))
#     print(num)
# except ValueError:
#     print("Вы должны ввести число")

isUserInput = False
while not isUserInput:
    try:
        num = int(input("Enter num: "))
        isUserInput = True
        print(num)
    except ValueError:
        print("Вы должны ввести число")
