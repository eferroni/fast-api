
class AuthException(Exception):
    def __init__(self, message="Auth exception", status=400):
        super().__init__(message, status)
        self.message = message
        self.status = status


class AuthTokenException(AuthException):
    def __init__(self, message="Could not validate credentials"):
        self.status = 401
        super().__init__(message, self.status)


class AuthUnauthorizedException(AuthException):
    def __init__(self, message="Invalid credentials"):
        self.status = 401
        super().__init__(message, self.status)
