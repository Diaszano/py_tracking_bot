"""
Este módulo é responsável por fornecer os modelos de dados do banco de dados.

Ele contém definições para os modelos de dados utilizados pelo sistema, oferecendo uma estrutura base comum
e funcionalidades adicionais para lidar com timestamps de criação e atualização.
"""

from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base


class Base(declarative_base()):
    """
    Classe base para todos os modelos.

    Define colunas comuns para timestamps de criação e atualização.
    """

    __abstract__ = True

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment='Última data de atualização dos dados',
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment='Data de criação dos dados',
    )

    def __repr__(self) -> str:
        """
        Retorna uma representação de string do objeto.

        Esta função é usada principalmente para debug e logging.

        Retorna:
            str: Uma representação de string do objeto.
        """
        string = f'{self.__class__.__name__}('
        length = self.__dict__.__len__()
        for key, value in self.__dict__.items():
            length -= 1
            if '_sa_instance_state' not in key:
                string += f'{key!r}: {value!r}'
                if length >= 1:
                    string += ', '
        string += ')'
        return string


from .tracking import Tracking
from .user import User

__all__ = ('Base', 'Tracking', 'User')
