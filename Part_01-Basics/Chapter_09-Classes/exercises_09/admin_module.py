class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def describe_user(self):
        print(f'Username:  {self.username}  //  Password:  {self.password}')

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.access = True
    
    def does_user_have_access(self):
        if self.access:
            print('Yes, the user has access.')