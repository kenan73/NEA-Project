import hashlib
from login_system import LoginSystem

class User:
    ''' User Class to create, store and retrieve User information'''
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password  
        
    def __str__(self):
        return f"username={self.user_name}"

class Users:
    def __init__(self):
        self.users = []  # This will store User instances
        self.login_system = LoginSystem()
    
    def add_user(self, user_name: str, password: str):
        if self.login_system.create_user(user_name, password):
            new_user = User(user_name, password)
            self.users.append(new_user)
            print("User created successfully!")
        else:
            print("Failed to create user.")
    
    def log_in_user(self, user_name: str, password: str):
        if self.login_system.log_in(user_name, password):
            print("Logged in successfully!")
        else:
            print("Login failed.")
    
    def __str__(self):
        return '\n'.join(str(user) for user in self.users)

# Example usage
if __name__ == "__main__":
    users = Users()
    users.add_user("user1", "password123")
    users.log_in_user("user1", "password123")


