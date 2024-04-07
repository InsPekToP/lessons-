#2main4_2s
#Самостоятельная работа
# Создайте класс Rectangle с полями width и height.

# Реализуйте магический метод __str__, который возвращает строковое
# представление прямоугольника в формате "Ширина x Высота".
# Реализуйте магический метод __add__, который позволяет сложить
# два прямоугольника (два объекта на основе этого класса). Выполняйте добавление width и height.
# Создайте два объект класса Rectangle и сложите их, затем выведите результат в консоль.


class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Ширина {self.width} x Высота {self.height}"
    
    def __add__(self,other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width,new_height)
    

rect1 = Rectangle(4,6)
rect2 = Rectangle(2,3)

result = rect1 + rect2

print(f'Результат сложения: {result}')
