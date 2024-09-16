from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(_):
    yield

app = FastAPI(lifespan=lifespan)