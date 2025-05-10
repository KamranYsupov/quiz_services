import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TelegramBaseSchema(BaseModel):
    telegram_id: int
    username: Optional[str]
    fullname: str


class TelegramUserSchema(TelegramBaseSchema):
    id: uuid.UUID
    quiz_answer: Optional[int] = None


class TelegramCreateUserSchema(TelegramBaseSchema):
    pass

