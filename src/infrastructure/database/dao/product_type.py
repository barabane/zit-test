from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import ProductType


class ProductTypeDao:
    @staticmethod
    async def get_by_id(type_id: int):
        async with async_session_maker() as session:
            return await session.get(ProductType, type_id)
