import hashlib
import database

class LoginSystem:
    def __init__(self):
        pass
    
    def hash_password(self, password: str) -> str: # Using hashlib for password hashing
        return hashlib.sha256(password.encode()).hexdigest()

    def validate_user_name(self, user_name: str) -> bool: # Checks if username meets requirements
        return all(c.islower() or c.isdigit() or c == '_' for c in user_name)

    def create_user(self, user_name: str, password: str) -> bool:
        if not self.validate_user_name(user_name):
            print("Invalid username.")
            return False
        
        if not database.username_is_unique(user_name):
            print('Username already exists.')
            return False 
      
        hashed_password = self.hash_password(password)
        
        return True

    def log_in(self, user_name: str, password: str) -> bool:
        # Hash the password for login attempt and compare with stored hash
        hashed_password = self.hash_password(password)
        return self.login_details.get(user_name) == hashed_password
    
login_system = LoginSystem()

# Example usage
user_name = str(input('Enter username: '))
password = str(input('Enter password '))
login_system.create_user(user_name, password)
