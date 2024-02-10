from login_system import LoginSystem


class User():
    ''' User Class to create,store and retive User information'''
    def __init__(self):
        self.user = ""
        self.password = ""
        
    def new(self):
        '''Create new User'''
        user = input()
        password = input()

        login_system.create_user(user, password)
    
    def __str__(self):
        return f"username ={self.user} password={self.password}"
        
# Composite Class of Users
class Users(LoginSystem):
    def __init__(self):
        super().__init__(self)
    
if __name__ == "__main__":
    kenan = User()
    kenan.new()
    print(kenan)
    
    game_users = Users()
    

