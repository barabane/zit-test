from src.application.domain.product import ProductCreate
from src.exceptions import ProductNotFoundException, ProductTypeDoesNotExists
from src.infrastructure.database.dao.product_dao import ProductDao
from src.infrastructure.database.dao.product_type import ProductTypeDao
from src.infrastructure.database.models import Product


class ProductService:
    async def get_all(self) -> list[Product]:
        return await ProductDao.get_all()

    async def create(self, product_data: ProductCreate) -> Product:
        type_exists = await ProductTypeDao.get_by_id(product_data.product_type_id)
        if not type_exists:
            raise ProductTypeDoesNotExists

        return await ProductDao.create(product_data)

    async def get_by_id(self, id: int) -> Product | None:
        product = await ProductDao.get_by_id(id)

        if not product:
            raise ProductNotFoundException

        return product

    async def get_by_type_id(self, type_id: int) -> list[Product]:
        type_exists = await ProductTypeDao.get_by_id(type_id)
        if not type_exists:
            raise ProductTypeDoesNotExists

        return await ProductDao.get_by_type_id(type_id)
