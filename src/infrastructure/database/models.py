from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.database import Base


class ProductType(Base):
    __tablename__ = "product_type"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False)


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR, nullable=False)
    product_type_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("product_type.id"))
