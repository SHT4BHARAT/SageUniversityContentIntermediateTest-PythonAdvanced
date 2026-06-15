f=open("report.txt","w")
f.write("Rahul-45\n")
f.write("Priya-90\n")
f.write("Rohan-78\n")
f.write("Sneha-92\n")
f.write("Amit-65\n")
f.close()


try:
    f = open("report.txt", "r")
    for line in f:
        name, marks = line.strip().split('-')
        if int(marks) > 80:
            print(f'{name}-{marks}')
except FileNotFoundError:
    print('Error: File not found')
finally:
    print('File handling complete')