class UserException(Exception):
    def __init__(self, message="User exception", status=400):
        super().__init__(message, status)
        self.message = message
        self.status = status


class UserNotFound(UserException):
    def __init__(self, message="User not found"):
        self.status = 404
        super().__init__(message, self.status)


class UserAlreadyExist(UserException):
    def __init__(self, message="User already exist"):
        self.status = 422
        super().__init__(message, self.status)


class UserValueError(UserException):
    def __init__(self, message="User value error"):
        self.status = 400
        super().__init__(message, self.status)


class UserInactive(UserException):
    def __init__(self, message="Inactive User"):
        self.status = 400
        super().__init__(message, self.status)
