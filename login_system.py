import hashlib
import mysql.connector

class LoginSystem:
    def __init__(self):
        self.login_details = {}

    def hash_password(self, password: str) -> str: # Using hashlib for password hashing.
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_user_name(self, user_name: str) -> bool:
        return all(c.islower() or c.isdigit() or c == '_' for c in user_name)

    def create_user(self, user_name: str, password: str) -> bool:
        if user_name in self.login_details:
            print("Username already exists.")
            return False
        if not self.validate_user_name(user_name):
            print("Invalid username.")
            return False
        hashed_password = self.hash_password(password)
        self.login_details[user_name] = hashed_password
        return True

    def log_in(self, user_name: str, password: str) -> bool:
        hashed_password = self.hash_password(password)
        return self.login_details.get(user_name) == hashed_password

# Example usage
login_system = LoginSystem()
if login_system.create_user("user1", "password123"):
    print("User created successfully!")
else:
    print("Failed to create user.")

if login_system.log_in("user1", "password123"):
    print("Logged in successfully!")
else:
    print("Login failed.")


'''user1 = LoginSystem()
user1.create_user("kenan", "123")
print(user1.log_in("kenan", "1234"))'''

