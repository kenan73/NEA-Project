import hashlib
import database

class LoginSystem:
    def __init__(self):
        pass
    
    def hash_password(self, password: str) -> str: # Using hashlib for password hashing
        global hashed_password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
    
    def validate_user_name(self, user_name: str) -> bool: # Checks if username meets requirements
        return all(c.islower() or c.isdigit() or c == '_' for c in user_name)
    
    def create_user(self, user_name: str, password: str) -> bool:
        if not self.validate_user_name(user_name):
            print('Invalid username.')
            return False
        
        if not database.username_is_unique(user_name):
            print('Username already exists.')
            return False
          
        hashed_password = self.hash_password(password)  
        
        if not database.insert_user_details(user_name, hashed_password):
            print('Failed to insert data')
        
        else:
            print('Data inserted successfully.')
        #Revise logic (else statement)
        
        return True
        
        
    def log_in(self, user_name: str, password: str) -> None: #Logs in user if details are verified
        self.hash_password(password)
        if database.verify_user_login(user_name, hashed_password):
            print('Successfully logged in.')
        else:
            print('User not found.')
        

login_system = LoginSystem()

# Example usage
run = True
while run == True:
    user_name = str(input('Enter username: '))
    password = str(input('Enter password '))
    login_system.log_in(user_name, password)
