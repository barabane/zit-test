from fastapi import HTTPException

class BaseException(HTTPException):
    def __init__(self, status_code: int, detail: str = None) -> None:
        super().__init__(status_code, detail)