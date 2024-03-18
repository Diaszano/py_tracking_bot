from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    String,
    Uuid,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(
        Uuid, primary_key=True, server_default=text('gen_random_uuid()')
    )
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    trackings = relationship('Tracking', back_populates='user')
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


class Order(Base):
    __tablename__ = 'orders'

    id = Column(
        Uuid, primary_key=True, server_default=text('gen_random_uuid()')
    )
    code = Column(String(length=13), nullable=False, unique=True)
    trackings = relationship('Tracking', back_populates='order')
    data = Column(JSONB, nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )


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
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
