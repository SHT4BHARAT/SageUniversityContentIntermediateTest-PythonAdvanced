students = {
    'name': ['Rahul', 'Priya', 'Rohan'],
    'age': [25, 22, 28],
    'marks': [85, 90, 78]
}

students['name'].append('Sonia')
students['marks'][1] = 95

del students['age'][2]
print('Is "marks" key present?', 'marks' in students)

print('\nKeys:', list(students.keys()))
print('Values:', list(students.values()))
print('Items:', list(students.items()))

student_names = list(students.keys())
print('\nStudent names list:', student_names)