#main10_1s
#Работа с файлами
#user = input ("Enter data:")


# #f = open('data/file.txt','w') # - перезаписывает
# f = open('data/file.txt','a') # - добавляет
# # f.write('Some text\n Some new text')
# f.write(user + "\n")
# f.close()



f = open('data/file.txt', 'r')
#print(f.read(10)) #кол-во символов,кот. читает прога
for line in f:
    print(line,end="")

f.close()
