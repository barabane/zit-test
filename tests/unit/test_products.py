import pytest
from httpx import AsyncClient


async def test_getting_all_products(client: AsyncClient):
    response = await client.get("/products/")

    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "iphone 11", "product_type_id": 1},
        {"id": 2, "name": "macbook pro", "product_type_id": 2},
        {"id": 3, "name": "airpods", "product_type_id": 3},
    ]


@pytest.mark.parametrize(
    "name,product_type_id,status_code",
    [("iphone 12", 1, 200), ("iphone 12", 0, 422), ("i", 1, 422)],
)
async def test_create_product(client: AsyncClient, name, product_type_id, status_code):
    response = await client.post(
        "/products/", params={"name": name, "product_type_id": product_type_id}
    )
    assert response.status_code == status_code


@pytest.mark.parametrize("id,status_code", [(1, 200), (2, 200), (0, 404), (-1, 404)])
async def test_get_product_by_id(client: AsyncClient, id, status_code):
    response = await client.get(f"/products/{id}")
    assert response.status_code == status_code


@pytest.mark.parametrize(
    "type_id,status_code", [(1, 200), (2, 200), (0, 422), (-1, 422)]
)
async def test_get_products_by_type_id(client: AsyncClient, type_id, status_code):
    response = await client.get(f"/products/type/{type_id}")
    assert response.status_code == status_code
