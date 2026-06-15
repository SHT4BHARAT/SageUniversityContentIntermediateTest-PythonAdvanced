students = ['Rahul', 'Raj', 'Rakesh', 'Rohit', 'Rohan']
students.append('Sobhit')
students.insert(0, 'Shivansh')
students.remove('Raj')
dele = students.pop(2)
students.sort()
print('Reversed sorted list:', students[::-1])
print('First 3 elements:', students[:3])