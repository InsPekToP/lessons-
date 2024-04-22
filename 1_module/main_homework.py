#main_homework.py
# У вас есть следующий список:

# str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]
# Переберите его через цикл/циклы и сделайте одну общую переменную, 
#которая будет содержать все элементы списка. По итогу в консоль должна быть выведена строка, что будет содержать текст:

# some special text for you - 50

str_list = [["some", "special"], ["text", "for", "you"], ["-", 50]]

for i in str_list:
    for el in i:
        print(el,end=' ')
