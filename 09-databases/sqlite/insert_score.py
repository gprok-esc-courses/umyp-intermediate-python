import sqlite3

db = sqlite3.connect('scores.db')

username = input("Username: ")
dt = input("Date and Time: ")
score = int(input("Score: "))

statement = """
            INSERT INTO scorers (username, date_time, score)
            VALUES (?, ?, ?)
            """
arguments = (username, dt, score)
db.execute(statement, arguments)

db.commit()