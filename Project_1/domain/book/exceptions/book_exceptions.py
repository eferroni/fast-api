class BookException(Exception):
    def __init__(self, message="Book exception", status=400):
        super().__init__(message, status)
        self.message = message
        self.status = status


class BookNotFound(BookException):
    def __init__(self, message="Book not found"):
        self.status = 404
        super().__init__(message, status=self.status)


class BookIdAlreadyExist(BookException):
    def __init__(self, message="Book already exist"):
        self.status = 422
        super().__init__(message, status=self.status)
