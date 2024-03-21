"""
This package is responsible for configuring the database.

It provides all the necessary configurations to use the database in the system.
"""
from sqlalchemy.ext.asyncio import AsyncSession as Session

from .connection import Engine

__all__ = ('Engine', 'Session')
