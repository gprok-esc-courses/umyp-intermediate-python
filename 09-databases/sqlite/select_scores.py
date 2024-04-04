import sqlite3

db = sqlite3.connect('scores.db')

cursor = db.cursor()

result = cursor.execute("SELECT * FROM scorers ORDER BY date_time")

for row in result:
    print(row[1], row[3], row[2])