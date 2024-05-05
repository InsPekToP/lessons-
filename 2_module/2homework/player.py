#player.py
# from variants import Variants
 
 
# class Player:
#     def __init__(self, var=Variants.ROCK, name='Bot'):
#         self.name = name
#         self.var = var.value
 
#     def whoWins(self, first, second):
#         if first.var == second.var:
#             return 'НИЧЬЯ'
#         elif first.var == 'rock' and second.var == 'scissors' \
#                 or first.var == 'scissors' and second.var == 'paper' \
#                 or first.var == 'paper' and second.var == 'rock':
#             return f'Победил игрок с именем {first.name}'
#         else:
#             return f'Победил игрок с именем {second.name}'

#Правильный вариант
from variants import Variants

class Player:
    def __init__(self, choice=Variants.ROCK, name='Bot'):
        self.name = name
        self.choice = choice

    def whoWins(self, first, second):
        if first.choice == second.choice:
            return 'НИЧЬЯ'
        elif(first.choice==Variants.ROCK and second.choice == Variants.SCISSORS
             or (first.choice==Variants.SCISSORS and second.choice == Variants.PAPER)
             or (first.choice==Variants.PAPER and second.choice == Variants.ROCK)):
            return "Победил игрок с именем:" + first.name
        else:
            return "Победил игрок с именем:" + second.name
