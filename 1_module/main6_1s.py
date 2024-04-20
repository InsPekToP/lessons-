#main6_1s.py
#Циклы For,While.Операторы

#While
# i = 1000
# while i > 10:
#     print(f"Element:{i}")
#     i /= 5

# isRunning = True
# while isRunning:
#     user = int(input("Enter number 0:"))
#     if user == 0:
#         isRunning = False
# print("Finish")

#For

# for i in range(2,10,2):
#     print(f"Element:{i}")

#Работа со строками

# word = "Hello"
# for el in word:
#     if el == 'l': print("Found")

#Операторы в циклах(break,continue)

# for i in range(10,20):
#     if i%2 == 0: continue

#     print(f"Element:{i}")
#     if i == 15: break


#Операторы else для цикла

word = "Hello"
for el in word:
    if el == 'l':
        print("Found")
        break
else:
    print("Не нашли")

    
