f = open('employees.txt', 'w')
f.write('Alice\n')
f.write('Bob\n')
f.write('Charlie\n')

f = open('employees.txt', 'r')
print('Original content:')
print(f.read())

f = open('employees.txt', 'a')
f.write('David\n')
f.write('Eve\n')

f = open('employees.txt', 'r')
print('\nUpdated content:')
print(f.read())

import os
try:
    os.remove('employees.txt')
    if not os.path.exists('employees.txt'):
        print('\nFile deleted successfully')
    else:
        print('\nFile still exists')
except FileNotFoundError:
    print('\nFile does not exist')