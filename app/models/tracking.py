from sqlalchemy import Column, String, Uuid, text
from sqlalchemy.dialects.postgresql import JSONB

from . import Base


class Tracking(Base):
    """
    Data model for representing trackings.

    Esta classe define a estrutura de dados para os rastreamentos no sistema.
    """

    __tablename__ = 'trackings'
    __table_args__ = {'comment': 'Armazena todos os rastreamentos do sistema'}

    id = Column(
        Uuid,
        primary_key=True,
        server_default=text('gen_random_uuid()'),
        comment='Identificador único do rastreamento',
    )
    code = Column(
        String(length=13),
        nullable=False,
        unique=True,
        index=True,
        comment='Código único de rastreio dos correios',
    )
    data = Column(
        JSONB, nullable=False, comment='Dados do rastreamento da encomenda'
    )
