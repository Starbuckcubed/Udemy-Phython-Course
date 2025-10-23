#standard python library so no need to download
import sqlite3


dbfile= 'data.db'

#connect to database
conn = sqlite3.connect(dbfile)

#cursor object
cursor = conn.cursor()
#query
query = """
SELECT * FROM albums
WHERE Title LIKE '%Live%' AND LENGTH(Title) > 10  
"""
cursor.execute(query)
rows = cursor.fetchall()

#loop to make it look better
for row in rows:
    #give it a pattern using placeholders
    print(f'{row[0]}: {row[1]}')
#close connection
conn.close()