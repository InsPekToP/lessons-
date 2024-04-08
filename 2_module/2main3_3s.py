#2main3_3s
# Создайте главный класс Shape с полем color и пустым методом get_area().
# Создайте подкласс Circle, наследующийся от Shape.
# Добавьте поле radius и переопределите метод get_area() для вычисления площади круга –  3.14 * (радиус в квадрате).
# Создайте объект класса Circle с радиусом 5 и цветом "красный". Выведите его площадь в консоль.

class Shape():
    def __init__(self,color):
        self.color = color

    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, color,radius):
        # Вызов конструктора родительского класса.
        super().__init__(color)
        self.radius = radius
    
    def get_area(self):
        return 3,14*self.radius**2
    
red_circle = Circle('red',5)

print(f'Площадь круга {red_circle.get_area()}')
