import hashlib
from ..Backend import database

class LoginSystem:
    def __init__(self):
        pass
    
    def hash_password(self, password: str) -> str:
        '''Hashes the password using SHA-256.'''
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_user_name(self, user_name: str) -> bool:
        '''Checks if username meets all requirements.'''
        return len(user_name) <= 20 and all(c.islower() or c.isdigit() or c == '_' for c in user_name)

    
    def create_user(self, user_name: str, password: str) -> bool:
        '''Creates a new user if the credentials are valid and username doesn't already exist.'''
        if not self.validate_user_name(user_name):
            print('Invalid username.')
            return False
        
        if len(password > 20):
            print('Password must be 20 characters or less.')
            return False 
        
        if not database.username_is_unique(user_name):
            print('Username already exists.')
            return False
          
        hashed_password = self.hash_password(password)  
        
        try:
            if not database.insert_user_details(user_name, hashed_password):
                print('Failed to insert data.')
                return False
            else:
                print('User created successfully.')
                return True
        except Exception as e:
            print(f'Error creating user: {e}')
            return False
        
        
    def log_in(self, user_name: str, password: str) -> None: 
        '''Logs in user if details are verified.'''
        if len(password) > 20:
            print('Password must be 20 characters or less.')
            return False 
        
        hashed_password = self.hash_password(password)
        if database.verify_user_login(user_name, hashed_password):
            print('Successfully logged in.')
            return True 
        else:
            print('Username/password incorrect.')
            return False    

if __name__ == '__main__':
    login_system = LoginSystem()
    while True:
        choice = input("Do you want to (1) sign up or (2) log in? (Enter 1 or 2): ")
        user_name = input('Enter username: ')
        password = input('Enter password: ')

        if choice == '1':
            login_system.create_user(user_name, password)
        elif choice == '2':
            if login_system.log_in(user_name, password):
                print("Moving to main menu screen.")
                break