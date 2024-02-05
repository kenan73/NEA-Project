import mysql.connector

class LoginSystem:
    usernames = []
    passwords = []

    def __init__(self):
        pass

    def create_user(self, user_name, password):
        self.login_details = {'username':user_name,'password':password}
        self.usernames.append(user_name)
        self.passwords.append(password)
        
    def username_is_unique(self, user_name): # Returns bool (True/False)
        user_count = self.usernames.count(user_name)
        
        return user_count == 0
        
user1 = LoginSystem()
user1.create_user("kenan", "abc")
print(user1.login_details['username'], user1.login_details['password'])