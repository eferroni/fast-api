class PasswordException(Exception):
    def __init__(self, message="Password exception", status=400):
        super().__init__(message, status)
        self.message = message
        self.status = status


class PasswordPolicy(PasswordException):
    def __init__(self, message="Password must be between 8 and 16 character, and must have at least one lower character, one upper character e one digit"):
        self.status = 400
        super().__init__(message, self.status)
