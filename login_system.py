class LoginSystem:
    user_names = []
    passwords = []


    def __init__(self):
        pass
    
    def create_user(self, user_name, password):
        self.user_names.append(user_name)
        self.passwords.append(password)
    
    def username_is_unique(self, user_name): # Returns bool (True/False)
        user_count = self.user_names.count(user_name)
        
        return user_count == 0

        

        

    
    
    def some_print(self):
        print("HIII")

    # def user_name(self, user_names):
    #     se

# To test
        
system = LoginSystem()
system.create_user("gabriel", "abc")
print(f"{system.user_names}\n {system.passwords}")



