import psycopg2
dbname="hr"
user = "sulaim"


def load_leave_employee(dbname,user):
    connection = psycopg2.connect(f"dbname={dbname} user={user}")
    curs = connection.cursor()
    load_file=open('leave_insert.sql','r')
    curs.execute(load_file.read())

    connection.commit()
    curs.close()
    connection.close()
    print("done")
load_leave_employee(dbname,user)