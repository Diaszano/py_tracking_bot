from pydantic import BaseModel, PositiveInt


class UserCreate(BaseModel):
    telegram_id: PositiveInt
