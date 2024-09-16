from fastapi import APIRouter, Depends, Response, status

from src.application.services.product_service import ProductService
from src.presentation.api.products.schemas import SProductCreate

products_router = APIRouter(prefix="/products", tags=["Products"])


@products_router.get(path="/")
async def get_all(product_service: ProductService = Depends(ProductService)):
    return await product_service.get_all()


@products_router.post(path="/")
async def create(
    product_service: ProductService = Depends(ProductService),
    product_data: SProductCreate = Depends(SProductCreate),
):
    return await product_service.create(product_data)


@products_router.get(path="/{id}")
async def get_by_id(id: int, product_service: ProductService = Depends(ProductService)):
    product = await product_service.get_by_id(id)

    if not product:
        return Response(
            status_code=status.HTTP_404_NOT_FOUND,
            content=f"Product with id={id} not found",
        )
    return product


@products_router.get(path="/type/{type_id}")
async def get_by_type_id(
    type_id: int, product_service: ProductService = Depends(ProductService)
):
    return await product_service.get_by_type_id(type_id)
