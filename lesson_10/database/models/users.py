class User:
    def __init__(self, first_name, last_name, password):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return f"<User #{self.id}>"


class Contacts:
    def __init__(self, user_id, friend_id) -> None:
        self.id = None
        self.user_id = user_id
        self.friend_id = friend_id

    def __repr__(self):
        return f"<User #{self.friend_id} in contacts #{self.user_id}>"
