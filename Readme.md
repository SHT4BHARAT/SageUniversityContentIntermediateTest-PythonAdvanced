Gryphon Academy Pvt. Ltd.
Sage University Content
Intermediate Test — Python Advanced
Total Marks: 30
Time: 1 Hour

Date: June 2025

Section 1 — OOP (10 Marks)
Q1. Create a class Employee with: (3 Marks)
• Private variable __salary = 50000
• Method increment() fi salary += 10000
• Method deduct() fi salary -= 5000
• Method get_salary() fi print salary
Create 2 objects and call all methods on both.

Q2. Create Abstract class Vehicle with: (4 Marks)
• Abstract methods: start(), stop(), fuel_type()
Create 3 child classes:
• Car fi 'Car started' / 'Petrol'
• Bike fi 'Bike started' / 'Petrol'
• Tesla fi 'Tesla started' / 'Electric'
Create objects and call all methods.

Q3. Create a Hybrid Inheritance program: (3 Marks)
• Father: property(), business()
• Son(Father): study()
• Daughter(Father): dance()
• GrandChild(Son, Daughter): gaming()
Create object of GrandChild and call ALL methods.

Section 2 — Exception Handling (8 Marks)
Q4. Create class AgeVerification: (4 Marks)
• Method set_age(age):
fi If age < 0 : raise ValueError
fi If age < 18 : raise custom UnderAgeError
fi If age > 100 : raise custom InvalidAgeError
fi Else : print 'Valid age!'
• Handle all exceptions with finally block.

Q5. Create a Login System: (4 Marks)
• Private variable __password = 'python@123'
• Private variable __attempts = 3
• Method login(password):
fi Wrong password: attempts -= 1, show remaining
fi If attempts == 0: raise AccountLockedError
fi Correct: print 'Login successful!'
• Handle AccountLockedError with finally block.

Section 3 — File Handling (6 Marks)
Q6. Create a Student Report System: (3 Marks)
• Create 'report.txt' with 5 students and marks:
Rahul-85, Priya-90, Rohan-78, Sneha-92, Amit-65
• Read file and print only students with marks > 80
• Handle FileNotFoundError with finally block.

Q7. Create an Employee File System: (3 Marks)
• Create 'employees.txt' with 3 employees
• Read the file and print
• Append 2 more employees
• Read updated file
• Delete the file and verify using os.path.exists()

Section 4 — List, Set, Dictionary and Tuples (6 Marks)
Q8. Perform the following List operations: (2 Marks)
• Create a list of 5 student names
• Add 2 more names using append() and insert()
• Remove a name using remove() and delete by index using pop()
• Sort the list alphabetically and print it in reverse order
• Slice the list to print only the first 3 elements

Q9. Perform the following Set and Tuple operations: (2 Marks)
• Create a set of 5 programming languages (include 2 duplicates) — print to show uniqueness
• Create another set of 3 languages and perform: union, intersection, difference
• Create a tuple of 5 city names
• Count occurrences of a city, find its index, and check if a city exists in the tuple
• Try to modify the tuple and handle the error with a proper message

Q10. Perform the following Dictionary operations: (2 Marks)
• Create a dictionary of 3 students: {'name': ..., 'age': ..., 'marks': ...}
• Add a new student and update marks of an existing student
• Delete a student using del and check if a key exists using 'in'
• Loop through the dictionary and print all keys, values, and items
• Convert all student names to a list using dict.keys(