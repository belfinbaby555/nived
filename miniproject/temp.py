import sqlite3
import os

# Function to create a connection to the SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to insert data into the Teacher table
def insert_teacher(conn, place, image, season, category=None, type=None, stars=None):
    sql = ''' INSERT INTO main_data(place, image, season, category, type, stars)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (place, image, season, category, type, stars))
    return cur.lastrowid

# Path to your SQLite3 database file
db_file = 'db.sqlite3'

# Example data to insert
teachers_data = [
    ("kannur", "image1.jpg", "spring", "place", "individual", "4.5"),
    ("goa", "image2.jpg", "summer", "travel", "couple", "5"),
    # Add more data as needed
]

# Create a connection to the database
conn = create_connection(db_file)

if conn is not None:
    # Insert data into the Teacher table
    for data in teachers_data:
        insert_teacher(conn, *data)
    conn.commit()
    conn.close()
    print("Data inserted successfully.")
else:
    print("Error! Cannot create the database connection.")
