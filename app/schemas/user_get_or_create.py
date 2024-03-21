from typing import Optional

from pydantic import UUID4

from .user_create import UserCreate


class UserGetOrCreate(UserCreate):
    id: Optional[UUID4] = None
