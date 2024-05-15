#main13_#8.py
word = 'Football, basketball, skate'
# print(word[1])
# print(len(word))
# print(word.count('!'))
# print(word.upper())
# print(word.isupper())
# print(word.lower())
# print(word.islower())
# print(word.capitalize())
# print(word.find('p'))
hobby = word.split(', ')
# print(hobby[1])
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
# print(hobby)

result = ', '.join(hobby)
print(result)
