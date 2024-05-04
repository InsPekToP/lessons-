#main11_#7.py
#функции
# numbers = [5,2,7]
# #numbers[3] = 100
# numbers.append(100)
# numbers.append(True)
#
# print(numbers)

# numbers = [5,2,7]
# numbers.append(100)
# numbers.insert(1,True)
#
# numbers.extend([5,6,8])
#
# print(numbers)

# numbers = [5,2,7]
# numbers.append(100)
# numbers.insert(1,True)
# b = [5,6,8]
# numbers.extend(b)
# numbers.sort()
#
# print(numbers)

numbers = [5,2,7]
numbers.append(100)
numbers.insert(1,True)
b = [5,6,8]
numbers.extend(b)
#numbers.reverse()
numbers.sort()

numbers.pop(-1)
#numbers.pop()
numbers.remove(6)

#numbers.clear()

#print(numbers.count(5))
print(len(numbers))
