class User():
    def __init__(self, user_id, name, access_level='user'):
        self.user_id = user_id
        self.name = name
        self.access_level = access_level

    def __str__(self):
        return f"User[ID={self.user_id}, Name={self.name}, Access Level={self.access_level}]"
class Admin(User):
    def __init__(self, user_id, name, admin_access_level='admin'):
        super().__init__(user_id, name, admin_access_level)
        self.users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self.users_list.append(user)
            print(f"Сотрудник {user.name} добавлен.")
        else:
            print("Недопустимый тип пользователя.")

    def remove_user(self, user_id):
        user_to_remove = next((user for user in self.users_list if user.user_id == user_id), None)
        if user_to_remove:
            self.users_list.remove(user_to_remove)
            print(f"Сотрудник {user_to_remove.name} удален.")
        else:
            print("Сотрудник не найден.")

    def list_users(self):
        print("Текущие пользователи:")
        for user in self.users_list:
            print(user)

if __name__ == "__main__":
    admin = Admin(user_id=1, name="Алиса")

    user1 = User(user_id=2, name="Михаил")
    user2 = User(user_id=3, name="Владимир")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.list_users()

    admin.remove_user(user_id=2)

    admin.list_users()

