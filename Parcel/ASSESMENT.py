import json

class User:
    def __init__(self, username, password, role='operator'):
        self.username = username
        self.password = password
        self.role = role

class UserManagementSystem:
    def __init__(self):
        self.users = []
        self.current_user = None

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                return True
        return False

    def add_user(self, username, password, role='operator'):
        user = User(username, password, role)
        self.users.append(user)

    def assign_admin_role(self, index):
        if 0 <= index < len(self.users):
            self.users[index].role = 'administrator'
        else:
            print("Invalid user index!")

    def remove_admin_role(self, index):
        if 0 <= index < len(self.users):
            self.users[index].role = 'operator'
        else:
            print("Invalid user index!")

    def delete_user(self, index):
        if 0 <= index < len(self.users):
            del self.users[index]
        else:
            print("Invalid user index!")

    def get_users_by_role(self, role):
        filtered_users = []
        for user in self.users:
            if user.role == role:
                filtered_users.append(user)
        return filtered_users

    def save_users_to_file(self):
        data = []
        for user in self.users:
            user_data = {
                'username': user.username,
                'password': user.password,
                'role': user.role
            }
            data.append(user_data)

        with open('users.json', 'w') as file:
            json.dump(data, file)

    def load_users_from_file(self):
        try:
            with open('users.json', 'r') as file:
                data = json.load(file)
                for user_data in data:
                    self.add_user(user_data['username'], user_data['password'], user_data['role'])
        except FileNotFoundError:
            pass

# Example usage
system = UserManagementSystem()
system.load_users_from_file()

# Logging in
username = input("Enter your username: ")
password = input("Enter your password: ")

if system.login(username, password):
    print("Login successful!")
    if system.current_user.role == 'administrator':
        print("Welcome, administrator:", system.current_user.username)
        print("What would you like to do?")
        print("1. Add user")
        print("2. Assign administrator role")
        print("3. Remove administrator role")
        print("4. Delete user")
        option = input("Enter the option number: ")

        if option == '1':
            new_username = input("Enter the username for the new user: ")
            new_password = input("Enter the password for the new user: ")
            new_role = input("Enter the role for the new user (default: operator): ")
            system.add_user(new_username, new_password, new_role)
            print("User added successfully!")
            system.save_users_to_file()

        elif option == '2':
            users = system.get_users_by_role('operator')
            print("Choose a user to assign as an administrator:")
            for i, user in enumerate(users):
                print(f"{i + 1}. {user.username}")
            user_index = int(input("Enter the user number: ")) - 1
            system.assign_admin_role(user_index)
            print("Administrator role assigned successfully!")
            system.save_users_to_file()

        elif option == '3':
            users = system.get_users_by_role('administrator')
            print("Choose a user to remove administrator role:")
            for i, user in enumerate(users):
                print(f"{i + 1}. {user.username}")
            user_index = int(input("Enter the user number: ")) - 1
            system.remove_admin_role(user_index)
            print("Administrator role removed successfully!")
            system.save_users_to_file()

        elif option == '4':
            print("Choose a user to delete:")
            for i, user in enumerate(system.users):
                print(f"{i + 1}. {user.username}")
            user_index = int(input("Enter the user number: ")) - 1
            system.delete_user(user_index)
            print("User deleted successfully!")
            system.save_users_to_file()

        else:
            print("Invalid option!")

    else:
        print("Welcome, operator:", system.current_user.username)
else:
    print("Login failed. Invalid username or password.")