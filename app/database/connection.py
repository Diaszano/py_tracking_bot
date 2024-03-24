"""
Este módulo é responsável por conectar-se ao banco de dados.

Fornece funcionalidades para criar o mecanismo do banco de dados.
"""

try:
    from config.enviroments import DATABASE_URL
except ImportError:
    from ..config.enviroments import DATABASE_URL
from sqlalchemy.ext.asyncio import create_async_engine

Engine = create_async_engine(DATABASE_URL.geturl())
