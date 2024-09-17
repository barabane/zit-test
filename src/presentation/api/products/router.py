from fastapi import APIRouter, Depends

from src.application.services.product_service import ProductService
from src.presentation.api.products.schemas import SProductCreate

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get(
    path="/",
    summary="Get all products",
    description="Get all products from database in a list",
)
async def get_all(product_service: ProductService = Depends(ProductService)):
    return await product_service.get_all()


@products_router.post(
    path="/",
    summary="Create new product",
    description="Create product from name and product type id",
)
async def create(
    product_service: ProductService = Depends(ProductService),
    product_data: SProductCreate = Depends(SProductCreate),
):
    return await product_service.create(product_data)


@products_router.get(
    path="/{id}",
    summary="Get product by id",
    description="Get product from database by id",
)
async def get_by_id(id: int, product_service: ProductService = Depends(ProductService)):
    return await product_service.get_by_id(id)


@products_router.get(
    path="/type/{type_id}",
    summary="Get all products by type",
    description="Get all product from database by type id",
)
async def get_by_type_id(
    type_id: int, product_service: ProductService = Depends(ProductService)
):
    return await product_service.get_by_type_id(type_id)
