class AuthService:
    def __init__(self, user_repository):
        self.current_user = None
        self.user_repository = user_repository

    def login(self, user_name, password):
        user = self.user_repository.find_user_by_name(user_name)
        if user is not None and user.password == password:
            self.current_user = user
        else:
            print("BAAAAAD user")

    def registration(self, user_name, password):
        self.user_repository.add_user(user_name, password)
        print("Success!!! Please login")

    def logout(self):
        print("Goodbye " + self.current_user.name)
        self.current_user = None

    def get_current_user(self):
        return str(self.current_user)
