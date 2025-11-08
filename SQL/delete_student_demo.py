import sqlite3

try:
    connection = sqlite3.connect("meinam_db.db")
    cursor = connection.cursor()
    delete_sql = "DELETE FROM student WHERE rollno = ?"
    delete_value = (1,)
    cursor.execute(delete_sql, delete_value)
    connection.commit()
    print("student deleted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()