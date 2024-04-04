import sqlite3

db = sqlite3.connect("scores.db")

db.execute(
        """CREATE TABLE IF NOT EXISTS scorers 
        ( \
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT NOT NULL,
            date_time TIMESTAMP NOT NULL,
            score INTEGER NOT NULL
        )"""
)

db.commit();
