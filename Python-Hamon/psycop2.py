import psycopg2


conn = psycopg2.connect("user=sulaim")
cur =conn.cursor()
initdb = "social"
cur.execute("create database "+initdb+";")
conn.commit()
cur.close()
conn.close()
