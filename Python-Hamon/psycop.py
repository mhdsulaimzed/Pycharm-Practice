




# conn = psycopg2.connect("dbname=hr user=sulaim") 
# cur = conn.cursor()
# # cur.execute( "CREATE TABLE employee (S_no SERIAL PRIMARY KEY,first_name VARCHAR(50),last_name VARCHAR(50) ,designation VARCHAR(50), email VARCHAR(50), phone VARCHAR(100) , company_address VARCHAR(100) );")
# # cur.execute("INSERT INTO employee (first_name,last_name,designation,email,phone,company_address) VALUES (%s,%s,%s,%s,%s,%s)",('sulaim','saed','software_developer','sulaimsaed@gmail.com','8590046766','hamon technologies'))
# cur.execute(    )
# conn.commit()
# cur.close()
# conn.close()






import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=test user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
...      (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()