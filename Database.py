import sqlite3

# Veritabanına bağlanma
conn = sqlite3.connect('ip_adresleri.db')
cursor = conn.cursor()

# Veritabanındaki verileri sorgulama
cursor.execute("SELECT * FROM ipadresleri")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
