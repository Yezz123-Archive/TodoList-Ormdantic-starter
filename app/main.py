from authx import ProfilerMiddleware
from fastapi import FastAPI

from app.db import _init_db
from app.routes import router

app = FastAPI(
    title="Ormdantic Starter",
    description="A starter project for Ormdantic",
    version="0.1.0",
    debug=True,
    openapi_url="/api/v1/openapi.json",
)

app.add_middleware(ProfilerMiddleware)
app.include_router(router, prefix="/api/v1")


async def main():
    await _init_db()


@app.get("/")
async def index():
    return {"message": "Starter to use Ormdantic with FastAPI"}
