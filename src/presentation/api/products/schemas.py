from fastapi import Query
from pydantic import BaseModel, Field


class SProduct(BaseModel):
    id: int = Query(title="ID", example=123)
    name: str = Field(title="Name")
    product_type_id: int = Field(title="Product type id")


class SProductCreate(BaseModel):
    name: str = Field(title="Name")
    product_type_id: int = Field(title="Product type id")
