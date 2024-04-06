#2main5_1s.py
#Перечисления "ENUM"(подсказки)
#Enumeretion - enum - перечисления --позволяет создать список,в кот. будут различные вар-ты
#кот. мы сможем выбрать для нашей цели(полезны для разработчика)
#В одном месте можем описать все возможные вар-ты,затем можем обратиться к перечислению(enum)
#и потом через точку можем обратиться к подсказкам

from enum import Enum #из модуля enum импортировали класс Enum

class Choices(Enum):
    #важно не прописывать методы и конструкторы,а только вар-ты(поля)
    Sweet = 1, #значения должны быть цифрами(после ставим запятую)
    Spicy = 2, #после можем устанавливать проверки и т.д.
    Ice = 3,
    Hot = 4,

print(Choices.Hot) #через точку показывает подсказки(Sweet,Spicy и т.д.)

# user_choice = Choices.Sweet
user_choice = Choices.Hot


if(user_choice == Choices.Sweet):
    print("User selected sweets")
elif(user_choice == Choices.Hot):
    print("User selected hot")
