
from app.db import _init_db
from app.routes import router
from authx import ProfilerMiddleware
from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/openapi.json")

app.add_middleware(ProfilerMiddleware)
app.include_router(router, prefix="/api/v1")


async def main():
    await _init_db()
