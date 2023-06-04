from functools import wraps
from typing import Any


class Log:
    def __init__(self, logger) -> None:
        self.logger = logger

    def __call__(self, func) -> Any:

        @wraps(func)
        def logging_info(*args, **kwargs):
            res = func(*args, **kwargs)
            self.logger.debug(
                f"Функция {func.__name__} вызвана из модуля {func.__module__}"
            )
            return res

        return logging_info
