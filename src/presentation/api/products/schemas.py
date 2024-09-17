from pydantic import BaseModel, Field


class SProduct(BaseModel):
    id: int = Field(title="ID")
    name: str = Field(title="Name")
    product_type_id: int = Field(title="Product type id")


class SProductCreate(BaseModel):
    name: str = Field(title="Name", min_length=3)
    product_type_id: int = Field(title="Product type id")
