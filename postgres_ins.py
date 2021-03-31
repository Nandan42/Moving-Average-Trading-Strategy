import csv
import psycopg2
conn = psycopg2.connect("host=localhost dbname=new_database user=postgres password=Nandan@20")
cur = conn.cursor()
with open('HINDALCO.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO HINDALCO VALUES (%s, %s, %s, %s, %s, %s, %s)",
        row
    )
conn.commit()