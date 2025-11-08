import sqlite3

try:
    connection = sqlite3.connect("meinam_db.db")
    cursor = connection.cursor()
    insert_table_query = """
        INSERT INTO student (name,email,course,cgpa) VALUES(?,?,?,?)
        """
    student_records = [
        ("justin","justin@gmail.com","ece",4.5),
        ("money","money@gmail.com","cse",5.7),
        ("tingloaba","ting@gmail","civil",9.5),
        ("tomba","tomba@gmail","cse",7.5)
        ]
    cursor.executemany(insert_table_query,student_records)
    connection.commit()
    print("all student record inserted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()