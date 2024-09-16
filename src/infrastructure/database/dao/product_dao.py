from sqlalchemy import select

from src.application.domain.product import ProductCreate
from src.infrastructure.database.database import async_session_maker
from src.infrastructure.database.models import Product, ProductType


class ProductDao:
    @staticmethod
    async def get_all() -> list[Product]:
        async with async_session_maker() as session:
            res = await session.execute(select(Product))
            return res.scalars().all()

    @staticmethod
    async def create(product_data: ProductCreate) -> Product:
        async with async_session_maker() as session:
            product = Product(
                name=product_data.name, product_type_id=product_data.product_type_id
            )
            session.add(product)
            await session.commit()
            return product

    @staticmethod
    async def get_by_id(id: int) -> Product | None:
        async with async_session_maker() as session:
            return await session.get(Product, id)

    @staticmethod
    async def get_by_type_id(type_id: int) -> list[Product]:
        async with async_session_maker() as session:
            query = (
                select(Product)
                .join(ProductType, Product.product_type_id == ProductType.id)
                .where(Product.product_type_id == type_id)
            )
            res = await session.execute(query)
            return res.scalars().all()
