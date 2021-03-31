import psycopg2
conn = psycopg2.connect("host=localhost dbname=new_database user=postgres password=Nandan@20")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE HINDALCO(
    datetime timestamp,
    close float,
    high float,
    low float,
    open float,
    volume integer,
    intrument text
)
""")
conn.commit()