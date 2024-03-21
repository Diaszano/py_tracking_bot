from sqlalchemy import BigInteger, Column, Uuid, text
from sqlalchemy.orm import relationship

from . import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(
        Uuid, primary_key=True, server_default=text('gen_random_uuid()')
    )
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    trackings = relationship('Tracking', back_populates='user')

    def __repr__(self) -> str:
        return f'User{super().__repr__()}'
