import csv

file = open('students.csv')

reader = csv.reader(file)

counter = 0
for row in reader:
    if counter > 0:
        print(row[2], row[3], row[-4])
    counter += 1