import mariadb
import sys

def username_is_unique(user_name):
    try:
        # Connect to MariaDB
        conn = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="NEAProject73",
            port=3306,
            database="nea_db"
        )
        cursor = conn.cursor()
        query = "SELECT username FROM login_details WHERE username = %s"
        
        cursor.execute(query, (user_name,))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if result:
            return False
        else:
            return True
            
    except mariadb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
    



