import asyncio
import json

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from src.config import settings
from src.infrastructure.database.database import Base, async_session_maker, engine
from src.infrastructure.database.models import Product, ProductType
from src.main import app as fastapi_app

settings.MODE = "TEST"


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"../tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)

    products = open_mock_json("products")
    product_types = open_mock_json("product_types")

    async with async_session_maker() as session:
        add_products = insert(Product).values(products)
        add_product_types = insert(ProductType).values(product_types)

        await session.execute(add_product_types)
        await session.execute(add_products)

        await session.commit()


@pytest.fixture(scope="session")
def event_loop_func(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=fastapi_app), base_url="http://test"
    ) as client:
        yield client
