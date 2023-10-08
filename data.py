import sqlite3

conn = sqlite3.connect('tickets.db')
cursor = conn.cursor()

# Create Tickets table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        used INTEGER DEFAULT 0
    )
''')

conn.commit()
conn.close()
