from decouple import config
from ormdantic import Ormdantic

DATABASE_URL = "sqlite+aiosqlite:///db.sqlite3" or config("DATABASE_URL")

db = Ormdantic(DATABASE_URL)


async def _init_db() -> None:
    async with db._engine.begin() as conn:
        await db.init()
        await conn.run_sync(db._metadata.drop_all)
        await conn.run_sync(db._metadata.create_all)
    return db
