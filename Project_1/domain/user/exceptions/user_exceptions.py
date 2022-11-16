class UserNotFound(KeyError):
    pass


class UserAlreadyExist(KeyError):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class UserValueError(ValueError):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


class PasswordPolicy(ValueError):
    def __init__(self, message="Password must be between 8 and 16 character, and must have at least one lower character, one upper character e one digit"):
        self.message = message
        super().__init__(self.message)
