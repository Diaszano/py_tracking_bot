from sqlalchemy import Column, String, Uuid, text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from . import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(
        Uuid, primary_key=True, server_default=text('gen_random_uuid()')
    )
    code = Column(String(length=13), nullable=False, unique=True)
    trackings = relationship('Tracking', back_populates='order')
    data = Column(JSONB, nullable=False)

    def __repr__(self) -> str:
        return f'Order{super().__repr__()}'
