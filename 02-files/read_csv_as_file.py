
file = open('students.csv')

lines = file.readlines()

headers = lines[0].strip().split(',')

print(headers)

for i in range(1, len(lines)):
    student_data = lines[i].strip().split(',')
    print(student_data[2], student_data[3])

