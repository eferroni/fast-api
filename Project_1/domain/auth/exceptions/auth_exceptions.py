from fastapi import HTTPException, status


class AuthTokenException(HTTPException):
    # invalid token
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Incorrect username or password",
                         headers={"WWW-Authenticate": "Bearer"})


class AuthUnauthorizedException(HTTPException):
    # unauthorized access
    def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail="Invalid credentials",
                         headers={"WWW-Authenticate": "Bearer"})
