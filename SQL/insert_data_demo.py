import sqlite3

try:
    connection = sqlite3.connect("meinam_db.db")
    cursor = connection.cursor()
    insert_table_query = """
        INSERT INTO student(name,email,course,cgpa) VALUES(?,?,?,?)
        """
    student_data = ("meinam","meinam@gmail.com","MCA","9.5")
    cursor.executemany(insert_table_query, student_data)
    connection.commit()
    print("student data inserted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
