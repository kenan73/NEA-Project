import mariadb
import sys

try:
    conn = mariadb.connect(
        host="127.0.0.1",
        user="root",
        password="NEAProject73",
        port=3306,
    )
    
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")

    for x in cursor:
        print(x)  # Assuming db is a tuple where the first item is the database name

except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)





