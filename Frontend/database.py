import mariadb
import sys

def connect():
    """Establishes a connection to the MariaDB database and returns the connection object."""
    try:
        conn = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="NEAProject73",
            port=3306,
            database="nea_db"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)



def username_is_unique(user_name: str):
    """Checks if there is a duplicate value stored in the database"""
    try:
        conn = connect()
        cursor = conn.cursor()
        query = "SELECT username FROM login_details WHERE username = %s"
        
        cursor.execute(query, [user_name])
        result = cursor.fetchone()
        
        if result:
            return False
        else:
            return True
    
    except mariadb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    finally:
        cursor.close()
        conn.close()
        

def insert_user_details(user_name: str, hashed_password: str) -> bool:
    """Inserts username and password into the login details database"""   
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO login_details (username, pssword) VALUES (?, ?)', (user_name, hashed_password))
        conn.commit()
        return True
 
        
    except mariadb.Error as e:
        print(f'Error inserting data into MariaDB: {e}')
        return False
        
    finally:
        cursor.close()
        conn.close()
        
        
def verify_user_login(user_name: str, hashed_password: str) -> bool:
    """Verifies if the provided username and password match the stored credentials in the database."""
    try:
        conn = connect()
        cursor = conn.cursor()
        
        
        query = 'SELECT pssword FROM login_details WHERE username = %s'
        cursor.execute(query, [user_name])
        result = cursor.fetchone()
         
        if result:
            stored_hashed_password = result[0]
            return stored_hashed_password == hashed_password
        
        else:
            return False
            
    except mariadb.Error as e:
        print(f'Error: {e}')
        sys.exit(1)
    
    finally:
        cursor.close()
        conn.close()
    



