class Port:
    def __init__(self):
        self._value = 7777

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (value >= 0):
            raise ValueError("Port must be >= 0")
        self._value = value
