from fastapi import HTTPException, status


class BaseException(HTTPException):
    def __init__(self, status_code: int, detail: str = None) -> None:
        super().__init__(status_code, detail)


class ProductTypeDoesNotExists(BaseException):
    def __init__(
        self, detail: str = "Product type with this id does not exists"
    ) -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail
        )


class ProductNotFoundException(BaseException):
    def __init__(self, detail: str = "Product with this id not found") -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
