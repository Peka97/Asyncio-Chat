class UserNotAuthorized(Exception):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "User must be authorized"
