import login_system


class User:
    def __init__(self):
        user = input()
        password = input()

        login_system.create_user(user, password)
        
# Composite Class of Users
class Users:
    self.login_details = {}