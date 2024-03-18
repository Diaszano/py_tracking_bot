from sqlalchemy.ext.asyncio import create_async_engine

from app.config.enviroments import DATABASE_URL

Engine = create_async_engine(DATABASE_URL.geturl())
