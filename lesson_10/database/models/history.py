class History:
    def __init__(self, ip, port) -> None:
        self.id = None
        self.logined_at = None
        self.ip = ip
        self.port = port

    def __repr__(self) -> str:
        return f"<{self.ip}>"
