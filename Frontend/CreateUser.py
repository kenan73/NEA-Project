'''from login_system import LoginSystem
def CreateUser():
    login_system = LoginSystem()
    while True:
        action = input("Do you want to (1) create an account or (2) log in? (Enter 1 or 2): ")
        if action not in ['1', '2']:
            print("Invalid option. Please enter 1 or 2.")
            continue

        user_name = input("Enter username: ")
        password = input("Enter password: ")

        if action == '1':
            login_system.create_user(user_name, password)
        elif action == '2':
            if login_system.log_in(user_name, password):
                # Proceed to the main part of your application
                print("Welcome to the system!")
                break  # Exit the loop after successful login
            else:
                print("Please try again.")

if __name__ == "__main__":
    CreateUser()'''
