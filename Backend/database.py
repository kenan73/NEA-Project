import mariadb

class Database:
    def connect(self):
        # TODO: use try catch block 

        conn = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="NEAProject73",
            port="3306"
        )

        cursor = conn.cursor()
        cursor.execute("SHOW DATABASES;")
        print(cursor)
        return cursor
    
    
        
if __name__ == "__main__":
    print("hi")
    a_db = Database()
    a_db.connect()




