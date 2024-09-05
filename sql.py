import sqlite3
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

cursor.execute('''
               Insert Into STUDENT (NAME, CLASS, SECTION, MARKS) 
               values ('Krish', 'CSE', 'A', 89),
               ('Yash', 'IT', 'B', 67),
               ('Kanishk', 'CSE', 'D', 60),
               ('Aarav', 'AI', 'C', 90),
               ('Vansh', 'CSE', 'A', 74),
               ('Isha', 'CCE', 'D', 80),
               ('Krishna', 'IT', 'C', 59),
               ('Yashwant', 'AI', 'D', 68),
               ('Kanishka', 'CSE', 'A', 88),
               ('Arnav', 'AI', 'B', 60),
               ('Vartika', 'CCE', 'D', 84),
               ('Ishan', 'CSE', 'A', 81)''')

table_info="""
Create table SUBJECT(CLASS VARCHAR(25),SUBJECT1 VARCHAR(25),
SUBJECT2 VARCHAR(25),PROGRAMMING VARCHAR(25));
"""
cursor.execute(table_info)

cursor.execute('''
               Insert Into SUBJECT (CLASS, SUBJECT1, SUBJECT2, PROGRAMMING) 
               values ('CSE', 'DSA', 'OOPS', 'C++'),
               ('IT', 'DSA', 'Web Dev', 'Java'),
               ('CCE', 'DSA', 'Networking', 'Java'),
               ('AI', 'ML', 'GenAI', 'Python')''')

print("STUDENT:")
data=cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)
print()
print("SUBJECT:")
data=cursor.execute('''Select * From SUBJECT''')
for row in data:
    print(row)

connection.commit()
connection.close()
