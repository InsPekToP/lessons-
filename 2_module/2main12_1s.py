#2main12_1s.py
#Управление компьютером pyautogui
#pip install PyAutoGUI

import pyautogui as pg
#import time

#pg.move(50,50,0.5) #ф-ия управления мышью(принимает 2 пар-ра:по координате X и Y)(относ. текущего положения)
#если запустить,то кажется ничего не происходит.Поэтому указываем 3й пар-тр,что добавляет плавность)

#pg.moveTo(200,300,0.5) #относ. края экрана(считаеся с левого верхнего угла)

#pg.drag(50,50,0.5,button = 'left') #мышь будет зажата,и выделять текст.

#print(pg.position()) #получаем координаты того места где мы хотим нажать.

#pg.click(139,90,duration=0.5) #кликаем мышью duration=0.5 = плавность
#pg.leftClick(139,90) #нажатие левой кномки мыши
#pg.rightClick(139,90) #правой
#pg.doubleClick(139,90,duration=0.5) #двойное нажатие

#Учимся печатать текст
# pg.typewrite("Hello word")
#Теперь открываем браузер и ищем координаты поисковой строки

# print(pg.position()) #Point(x=274, y=62) /Point(x=551, y=291)/(x=435, y=115)/x=418, y=285)

# pg.click(274,62,duration=0.5)
# pg.typewrite("youtube.com",0.1)
# pg.typewrite(["enter"])
# time.sleep(3)
# pg.click(435,115,duration=0.5)
# pg.typewrite("idi rabotaj kojaniu ubludok",0.1)
# pg.typewrite(["enter"])
# time.sleep(2)
# pg.click(418,285,duration=0.5)
# pg.typewrite(["enter"])


#Усложним задачу.Будем пользоваться горячими клавишами

# pg.hotkey("winleft") #нажимаем на кномку виндовс с лева
# pg.typewrite("chrome\n",0.5) #chrome\n - пишет хром и нажимает ентер
# pg.typewrite("www.youtube.com\n",0.2)
# pg.hotkey("winleft","up") #разворачиваем на весь экран
# pg.hotkey("ctrl","t") #открытие новой вкладки


# pg.alert("Some info message","Title message",button = "Button text") #создание всплывающих окон
# #.alert - вывод окна с информацией
# age = pg.prompt("Enter your age","You age")#для вывода информации от пользователя(можно записать в пер-ную
# print(age)
# pg.confirm("You are older than 18?","Are you sure?",("Yes,older","No"))#для окна с вопросами
# pg.password("Enter password","Password title")#получаем пароль от польз-ля

# import pyscreeze
# from PIL import Image
#Также можем сделать скриншот
#pg.screenshot("yourPic.png") #выбивает ошибку,что то с импортами связано


# t= pg.KEYBOARD_KEYS
# print(t)
