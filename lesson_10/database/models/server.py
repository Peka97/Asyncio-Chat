class User:
    def __init__(self, first_name, last_name, username, password):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.is_online = False

    def __repr__(self):
        return f"<User #{self.username}>"


class ServerHistory:
    def __init__(self, ip, port) -> None:
        self.id = None
        self.logined_at = None
        self.ip = ip
        self.port = port

    def __repr__(self) -> str:
        return f"<{self.ip}>"


class ServerContacts:
    def __init__(self, user_id, friend_id) -> None:
        self.id = None
        self.user_id = user_id
        self.friend_id = friend_id

    def __repr__(self):
        return f"<User #{self.friend_id} in contacts #{self.user_id}>"
