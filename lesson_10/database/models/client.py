class ClientContacts:
    def __init__(self, user_id) -> None:
        self.id = None
        self.user_id = user_id

    def __repr__(self):
        return f"<User #{self.user_id} in my contacts>"


class MessageHistory:
    def __init__(self, send_from, text) -> None:
        self.id = None
        self.send_from = send_from
        self.text = text
        self.dispatch_time = None

    def __repr__(self):
        return f"<Message #{self.id}>"
