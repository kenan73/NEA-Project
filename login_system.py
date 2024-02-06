import mysql.connector

class LoginSystem:
    login_details = {}
    
    def input_user_details():
        TODO: #add input details
    
    def validate_user_name(self, user_name: str):
        for c in user_name:
             if not (c.islower() or c.isdigit() or c == '_'):
                 return False
        return True

    def create_user(self, user_name: str, password: str) -> bool:
        if user_name in self.login_details:
            return False
        else:
            self.login_details.update({user_name: password})
            return True
            # TODO: Add logic for username already exists
    
    def log_in(self, user_name: str, password: str):
        if user_name in self.login_details:
            if self.login_details[user_name] == password:
                return True
        return False
            
        


        
        
        
        
    
    


        
    # def username_is_unique(self, user_name) -> bool: 
    #     user_count = self.usernames.count(user_name)
        
    #     return user_count == 0

user1 = LoginSystem()
user1.create_user("kenan", "123")
print(user1.log_in("kenan", "1234"))


""" TODO: 
        create_user()
        log_in()
"""
