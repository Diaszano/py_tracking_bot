"""
Este módulo contém a definição do modelo de dados para usuários.

Ele define a estrutura de dados para representar usuários no sistema, incluindo atributos como ID do Telegram.

Classes:
    Usuário: Classe que representa o modelo de dados para usuários.

Módulos Importados:
    BigInteger: Tipo de dado para armazenar números inteiros grandes.
    Column: Classe que define uma coluna em um modelo de dados SQLAlchemy.
    Uuid: Tipo de dado para armazenar identificadores únicos universais (UUIDs).
    text: Função para representar expressões SQL de texto literal.
    Base: Classe base para todos os modelos de dados do sistema.

Exemplo de Uso:
    from models.user import Usuário

    novo_usuario = Usuário(telegram_id=123456789)
    print(novo_usuario)
"""

from sqlalchemy import BigInteger, Column, Uuid, text

from . import Base


class User(Base):
    """
    Data model for representing users.

    Esta classe define a estrutura de dados para os usuários no sistema.
    """

    __tablename__ = 'user'
    __table_args__ = {'comment': 'Armazena todos os usuários do sistema'}

    id = Column(
        Uuid,
        primary_key=True,
        server_default=text('gen_random_uuid()'),
        comment='Identificador único do usuário',
    )
    telegram_id = Column(
        BigInteger,
        nullable=False,
        unique=True,
        index=True,
        comment='ID do Telegram do usuário',
    )
