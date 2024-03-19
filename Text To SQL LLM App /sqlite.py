import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''INSERT INTO STUDENT VALUES ('Samantha', 'Data Science', 'B', 75)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Rajesh', 'Data Science', 'A', 92)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Aisha', 'Data Science', 'B', 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Neha', 'Data Science', 'A', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ankit', 'DEVOPS', 'B', 60)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Priya', 'DEVOPS', 'A', 40)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Rohit', 'DEVOPS', 'B', 55)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Monica', 'DEVOPS', 'C', 30)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('David', 'Data Science', 'A', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Emma', 'Data Science', 'B', 78)''')


## Dispaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()