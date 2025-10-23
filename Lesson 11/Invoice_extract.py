#standard python library so no need to download
import sqlite3


dbfile= 'country_data.db'

#connect to database
conn = sqlite3.connect(dbfile)

#cursor object
cursor = conn.cursor()
#query
query = """
SELECT * FROM invoices
WHERE BillingCountry= 'Germany' AND Total >= 2  
"""
cursor.execute(query)
rows = cursor.fetchall()

#loop to make it look better
for row in rows:
    #give it a pattern using placeholders
    print(f'{row[0]}: {row[1]}')
#close connection
conn.close()