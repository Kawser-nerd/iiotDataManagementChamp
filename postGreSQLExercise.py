# TO connect the PostGreSQL database with Python interpreter, we need to install a connector, named psycopg2

# step 1: WE need to import the library
import psycopg2

# Step 2: We need to give/establish the server connection: this is names as server connection string
# For connection, we need to give the server address
conn = psycopg2.connect(host="localhost",
                        port="5432",
                        user="postgres",
                        database="postgres",
                        password="1234" # this is the server password.. once you logged in
                        # to the server, you can access any of the Database tables
                        )

# Step 3: Create a cursor.. A cursor is nothing just a pointer, which can access each
# rows in the table as well as each entity in the table.. Cursor mainly helps to read the
# entries from a table
# Another advantage of the cursor is to execute CRUD SQL queries in the database
cursor = conn.cursor()

# Step 4: Execute a Normal Query, lets say selection Query
sqlQuery1 = "SELECT temperature, humidity, light From occupancy ORDER BY date ASC LIMIT 10;"
cursor.execute(sqlQuery1) # this will help you to execute the query in the database server
# and will help you to retrieve the result back from the DB server

# Step 5: Collect the results of the query execution
'''
We need to use two methods to retrieve the results of the cursur execution queries
1. fetchone() : THis method will read only the first row of the resulted table/
2. fetchall() : THis method will read all the records from the query result
'''
results = cursor.fetchall()

# Step 6: Print or work with the result you got after executing your queries
# fetchone and fetchall(), both the methods return the values from the query as list
# the values present in the results variable are in a list
#print(results)

# Update operation

sqlQuery2 = ("SELECT occupancy, temperature, humidity from occupancy "
             "where date='2015-02-02 14:19:00' or date='2015-02-02 14:19:59'")

cursor.execute(sqlQuery2)
results2 = cursor.fetchall()
print(results2)

# update query
sqlQueryUpdate = ("Update occupancy set occupancy=0 "
                  "where date='2015-02-02 14:19:00' or date='2015-02-02 14:19:59'")
cursor.execute(sqlQueryUpdate)

# when you will change, update something in a table, you need to commit it
conn.commit()
print(cursor.statusmessage)

sqlQuery2 = ("SELECT occupancy, temperature, humidity from occupancy "
             "where date='2015-02-02 14:19:00' or date='2015-02-02 14:19:59'")

cursor.execute(sqlQuery2)
results2 = cursor.fetchall()
print(results2)

