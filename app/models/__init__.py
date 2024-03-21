from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import declarative_base


class Base(declarative_base()):
    __abstract__ = True

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    def __repr__(self) -> str:
        length = self.__dict__.__len__()
        string = '('
        for key, value in self.__dict__.items():
            length -= 1
            if '_sa_instance_state' not in key:
                string += '{}: {}'.format(key, value)
                if length >= 1:
                    string += ', '
        string += ')'
        return string


from .order import Order
from .tracking import Tracking
from .user import User

__all__ = ('Base', 'Order', 'User', 'Tracking')
