from src.application.domain.product import ProductCreate
from src.infrastructure.database.dao.product_dao import ProductDao
from src.infrastructure.database.models import Product


class ProductService:
    async def get_all(self) -> list[Product]:
        return await ProductDao.get_all()

    async def create(self, product_data: ProductCreate) -> Product:
        return await ProductDao.create(product_data)

    async def get_by_id(self, id: int) -> Product | None:
        return await ProductDao.get_by_id(id)

    async def get_by_type_id(self, type_id: int) -> list[Product]:
        return await ProductDao.get_by_type_id(type_id)
