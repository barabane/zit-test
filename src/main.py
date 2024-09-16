from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.presentation.api.products.router import products_router


@asynccontextmanager
async def lifespan(_):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(products_router)
