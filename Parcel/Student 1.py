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
            user = self.users[index]
            if user.role != 'administrator':
                user.role = 'administrator'
                print("Administrator role assigned successfully!")
            else:
                print("User already has administrator role.")
        else:
            print("Invalid user index!")

    def remove_admin_role(self, index):
        if 0 <= index < len(self.users):
            user = self.users[index]
            if user.role == 'administrator':
                user.role = 'operator'
                print("Administrator role removed successfully!")
            else:
                print("User does not have administrator role.")
        else:
            print("Invalid user index!")

    def delete_user(self, index):
        if 0 <= index < len(self.users):
            del self.users[index]
            print("User deleted successfully!")
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

system = UserManagementSystem()
system.load_users_from_file()
while True:
    # Logging in
    username = input("Enter your username (or type 'exit' to quit): ")
    if username.lower() == 'exit':
        break

    password = input("Enter your password: ")

    if system.login(username, password):
        if system.current_user.role == 'administrator':
            print("Welcome, Administrator:", system.current_user.username)
        else:
            print("Welcome, Operator:", system.current_user.username)

        while True:
            if system.current_user.role == 'administrator':
                print("What would you like to do?")
                print("1. Add user")
                print("2. Assign administrator role")
                print("3. Remove administrator role")
                print("4. Delete user")
                print("5. List of users")
                print("6. Logout")
                option = input("Enter the option number: ")

                #adding new user
                if option == '1':
                    new_username = input("Enter the username for the new user: ")
                    new_password = input("Enter the password for the new user: ")
                    new_role = input("Enter the role for the new user (default: operator): ")
                    system.add_user(new_username, new_password, new_role)
                    print("User added successfully!")
                    system.save_users_to_file()

                    #Assigning admin role
                elif option == '2':
                    users = system.get_users_by_role('operator')
                    if len(users) == 0:
                        print("No operators available to assign as administrators.")
                    else:
                        print("Choose a user to assign as an administrator:")
                        for i, user in enumerate(users):
                            print(f"{i + 1}. {user.username} (Role: {user.role})")
                        user_index = int(input("Enter the user number: ")) - 1
                        system.assign_admin_role(user_index)
                        system.save_users_to_file()

                #removing admin role
                elif option == '3':
                    users = system.get_users_by_role('administrator')
                    if len(users) == 0:
                        print("No administrators available to remove the role.")
                    else:
                        print("Choose a user to remove administrator role:")
                        for i, user in enumerate(users):
                            print(f"{i + 1}. {user.username} (Role: {user.role})")
                        user_index = int(input("Enter the user number: ")) - 1
                        system.remove_admin_role(user_index)
                        system.save_users_to_file()

                        #Deleting user
                elif option == '4':
                        print("Choose a user to delete:")
                        for i, user in enumerate(system.users):
                            print(f"{i + 1}. {user.username}")
                        user_index = int(input("Enter the user number: ")) - 1
                        system.delete_user(user_index)
                        system.save_users_to_file()

                        #Filtering users
                elif option == '5':
                    filter_option = input("Filter users by role (admin/operator/all): ")
                    #Filtering for admin only
                    if filter_option.lower() == 'admin':
                        users = system.get_users_by_role('administrator')
                        print("List of administrators:")
                        for i, user in enumerate(users):
                            print(f"{i + 1}. {user.username} (Role: {user.role})")
                    #Filtering for operator only
                    elif filter_option.lower() == 'operator':
                        users = system.get_users_by_role('operator')
                        print("List of operators:")
                        for i, user in enumerate(users):
                            print(f"{i + 1}. {user.username} (Role: {user.role})")
                    #Filtering all users
                    elif filter_option.lower() == 'all':
                            print("List of all users:")
                            for i, user in enumerate(system.users):
                                print(f"{i + 1}. {user.username} (Role: {user.role})")
                    #In case user typo
                    else:
                        print("Invalid filter option!")

                elif option == '6':
                    print("Logging out...")
                    break

                else:
                    print("Invalid option!")

            else:
                print("What would you like to do?")
                print("1. Logout")
                option = input("Enter the option number: ")

                if option == '1':
                    print("Logging out...")
                    break

                else:
                    print("Invalid option!")
    else:
        print("Login failed. Invalid username or password.")