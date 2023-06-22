class Port:
    def __set__(self, instance, value):
        if not (value >= 0):
            raise ValueError("Port must be >= 0")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
