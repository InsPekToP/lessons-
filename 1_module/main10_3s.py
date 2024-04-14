#main10_3s
#Обработка файлов

# try:
#     num = int(input("Enter num: "))
#     f = open('data/filex{num}.txt', 'r') #закинули то что ввел пользователь в название файла
#     print(f.read())

#     f.close()
# except FileNotFoundError:
#     print('Файл не найден')
# except ValueError:
#     print("Вы должны ввести число")
# finally:                                #выводится всегда
#     print("Finish")

#Оператор with...as
    
try:
    num = int(input("Enter num: "))
    with open(f'data/file{num}.txt', 'r',encoding = 'utf-8') as f: #encoding = 'utf-8' - позволяет считывать кирилицу и латинницу
        print(f.read())

except FileNotFoundError:
    print('Файл не найден')
except ValueError:
    print("Вы должны ввести число")
finally:                                #выводится всегда
    print("Finish")
