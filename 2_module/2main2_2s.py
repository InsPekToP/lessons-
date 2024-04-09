#2main2_2s
# Самостоятельная работа

# Создайте класс Book, представляющий книгу. Класс должен иметь поля: title, author и is_available.

# Добавьте метод check_out(), который устанавливает значение is_available в False, представляя,
# что книга взята в библиотеке.
# Добавьте метод check_in(), который устанавливает значение is_available в True, представляя,
# что книга возвращена в библиотеку.
# Создайте объект класса Book с названием "The Great Gatsby", автором "F. Scott Fitzgerald" 
#и установите начальное значение is_available в True.
# Выведите в консоль информацию о книге, затем проведите операцию аренды (check_out)
# и ещё раз выведите информацию о книге.

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        self.is_available = False
        print(f'Книга "{self.title}" взята в библиотеке.')
    
    def check_in(self):
        self.is_available = True
        print(f'Книга "{self.title}" возвращена в библиотеку.')

kniga = Book('The Great Gatsby','F. Scott Fitzgerald')
print(f'Информация о книге: Название - "{kniga.title}", Автор - "{kniga.author}", Доступность - {kniga.is_available}')
kniga.check_out()
print(f'Информация о книге после аренды: Название - "{kniga.title}", Автор - "{kniga.author}", Доступность - {kniga.is_available}')
