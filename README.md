# SQL Query Generation with Gemini AI

## Overview

This project provides a web application built using Streamlit that allows users to input natural language questions and receive corresponding SQL queries. The application leverages Google's Gemini AI to translate user questions into SQL queries, which are then executed on a SQLite database. The database contains two tables, `STUDENT` and `SUBJECT`, with sample data representing students and their respective subjects.

## Features

- **Natural Language to SQL Conversion**: Uses Google's Gemini AI to convert user-inputted questions into SQL queries.
- **SQLite Database**: A simple SQLite database (`student.db`) is used to store and retrieve data.
- **Interactive Web Interface**: Built with Streamlit, the interface allows users to input questions and see the results in real-time.

## Project Structure

- `app.py`: The main application script. It sets up the Streamlit web app, connects to the SQLite database, and handles interactions between the user input and the AI-generated SQL queries.
- `sql.py`: This script sets up the SQLite database. It creates the `STUDENT` and `SUBJECT` tables and populates them with sample data.
- `.env`: Environment file (not included in the repository) to store sensitive information such as the Google API key.
- `requirements.txt`: A file listing all necessary Python packages to run the project.

## Getting Started

### Prerequisites

- Python 3.x
- Google Cloud account (to use the Generative AI services)
- SQLite (comes pre-installed with Python)
- Streamlit

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/vedzzz28/Text-to-SQL-Generator
   cd Practise
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Google API key:

   ```bash
   GOOGLE_API_KEY=your-google-api-key
   ```

4. **Run the Database Setup Script**

   Before running the application, ensure the SQLite database is set up by executing:

   ```bash
   python sql.py
   ```

   This will create the `student.db` database with the required tables and sample data.

5. **Run the Application**

   Launch the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

   This will open the application in your web browser.

### Usage

1. Open the web application in your browser.
2. Enter a natural language question related to the student data, such as "List all students with their subject names."
3. Click the "Ask the question" button.
4. The application will display the corresponding SQL query's results.

### Examples of Supported Questions

- "How many entries of records are present?"
- "Tell me all the students studying in CSE class."
- "Find the students with Python as a programming language."
- "List all students with their subject names."

### Notes

- The Gemini AI service converts natural language into SQL queries based on the provided prompt. Ensure that your questions are structured clearly for the best results.
- The current version supports only the predefined tables (`STUDENT` and `SUBJECT`). Extending the prompt or adding more tables would require adjustments to the prompt and schema.


## Acknowledgments

- Google's Gemini AI for the natural language processing capabilities.
- Streamlit for providing an easy-to-use framework for building interactive web applications.

