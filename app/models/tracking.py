from sqlalchemy import BigInteger, Column, ForeignKey, String, Uuid
from sqlalchemy.orm import relationship

from . import Base


class Tracking(Base):
    __tablename__ = 'trackings'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(length=64), nullable=True)
    user_id = Column(Uuid, ForeignKey('users.id'), nullable=False)
    user = relationship(
        'User', back_populates='trackings', cascade='all, delete'
    )
    order_id = Column(Uuid, ForeignKey('orders.id'), nullable=False)
    order = relationship(
        'Order', back_populates='trackings', cascade='all, delete'
    )

    def __repr__(self) -> str:
        return f'Tracking{super().__repr__()}'
