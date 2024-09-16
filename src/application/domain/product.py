from typing import Optional

from pydantic import BaseModel


class ProductDto(BaseModel):
    id: Optional[int]
    name: Optional[str]
    product_type_id: Optional[int]


class ProductCreate(BaseModel):
    name: Optional[str]
    product_type_id: Optional[int]
