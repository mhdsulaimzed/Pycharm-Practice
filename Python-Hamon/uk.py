# 
import psycopg2

conn = psycopg2.connect("dbname=hr user=sulaim")

curs = conn.cursor()

curs.execute("SELECT * FROM employee")
datas = curs.fetchall()
ldata = []
for i in datas:
    ldata.append(list(i))
print(ldata)



conn.commit()
curs.close()






conn.close()