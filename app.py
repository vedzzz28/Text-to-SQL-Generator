from dotenv import load_dotenv
import os
load_dotenv()
import streamlit as st
import sqlite3
import google.generativeai as gen
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen.configure(api_key=GOOGLE_API_KEY)

def get_gemini_response(question,prompt):
    model=gen.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt=[
    """
You are an expert in converting english question to sql query. the sql database have the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.

For example,
example 1 - How many entries of records are present?, sql command will be something like SELECT COUNT(*) FROM STUDENT;
example 2 - Tell me all the student studying in CSE class?, sql command will be something like SELECT * FROM STUDENT where CLASS="CSE";
example 3 - Find the students with python as a programming?, sql command will be something like SELECT A.NAME, A.CLASS FROM STUDENT A, SUBJECT B where A.CLASS=B.CLASS AND B.PROGRAMMING="Python";
example 4 - Find the students with DSA as a subject?, sql command will be something like SELECT A.NAME, A.CLASS FROM STUDENT A, SUBJECT B where A.CLASS=B.CLASS AND (B.SUBJECT1="DSA" OR B.SUBJECT2="DSA");
example 5 - List all students with their subject names? SQL command will be something like: SELECT STUDENT.NAME, STUDENT.CLASS, STUDENT.SECTION, SUBJECT.SUBJECT1, SUBJECT.SUBJECT2, SUBJECT.PROGRAMMING FROM STUDENT INNER JOIN SUBJECT ON STUDENT.CLASS = SUBJECT.CLASS;

Make sure to use table aliases if columns are shared among tables, e.g., `STUDENT.CLASS`, `SUBJECT.SUBJECT_NAME`.

Also the sql code should not have ''' in the beginning or end and sql word in the output 
"""
]

st.set_page_config(page_title="SQL Query Generation")
st.header("Gemini app to generate sql data")
question=st.text_input("Input: ")
submit=st.button("Ask the question")
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)
