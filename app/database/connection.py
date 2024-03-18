"""
This module is responsible for connecting to the database.

Provides functionalities to create engine for the database.
"""
from sqlalchemy.ext.asyncio import create_async_engine

from ..config.enviroments import DATABASE_URL

Engine = create_async_engine(DATABASE_URL.geturl())
