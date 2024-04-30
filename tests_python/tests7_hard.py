#tests7_hard.py
# Ниже приведен сложный список, содержащий множество вложений. 
# Необходимо вывести на экран запись: «Why birds are not flying all the time?».

# Вам необходимо прописать логичные обращения к элементам и вывести элементы в таком порядке, 
# чтобы образовалась одна строка.

data = {
    'question': ['Why', 'are', 'not', 'all'],
    'animals': {
        'birds': [
            {'name': 'birds'}
        ],
        'others': [
            [
                {'name': 'flying'},
                {'name': 'the'},
                {'name': 'time'},
            ],
        ],
    },
    'parts': {
        'question': '?'
    }
}

print(data['question'][0],
      data['animals']['birds'][0]['name'],
      data['question'][1],
      data['question'][2],
      data['animals']['others'][0][0]['name'],
      data['question'][3],
      data['animals']['others'][0][1]['name'],
      data['animals']['others'][0][2]['name'],
      data['parts']['question'])
