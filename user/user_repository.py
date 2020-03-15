from user.user import User


class UserRepository:
    def __init__(self):
        self.users = {}
        self.add_user("A", "P")

    def add_user(self, user_name, password):
        user = User(user_name, password)
        self.users[str(user.id)] = user
        return user.id

    def find_user(self, id):
        return self.users.get(id)

    def find_user_by_name(self, name):
        for user in self.users.values():
            if user.name == name:
                return user

    def find_all(self):
        return self.users.values()

