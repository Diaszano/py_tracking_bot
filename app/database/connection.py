"""
This module is responsible for connecting to the database.

Provides functionalities to create engine for the database.
"""
try:
    from config.enviroments import DATABASE_URL
except ImportError:
    from ..config.enviroments import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine

Engine = create_async_engine(DATABASE_URL.geturl())
