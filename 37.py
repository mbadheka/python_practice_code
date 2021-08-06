students = {
    'malhar' : {'score': 90 , 'age' : 24},
    'tejas' : {'score': 82 , 'age' : 23},
    'abcd' : {'score': 76 , 'age'  : 25}
}

# print(students.get('tejas')['age'])

print(max(students, key= lambda i: students[i]['score']))

print(max.__doc__)