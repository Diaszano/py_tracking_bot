"""
Este pacote é responsável por configurar o banco de dados.

Ele fornece todas as configurações necessárias para utilizar o banco de dados no sistema.
"""

from sqlalchemy.ext.asyncio import AsyncSession as Session

from .connection import Engine

__all__ = ('Engine', 'Session')
