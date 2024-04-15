#main9_1s
#Генераторы в Python

# def generator(num):
#     while num > 0:
#         yield num
#         num -= 1

# val = generator(6)
# print(next(val))
# print(next(val))
# print(next(val))

def generator(lis):
    for i in lis:
        yield i


val = generator([6,9,2,5])
print(next(val))
print("Something")
print(next(val))
print(next(val))
