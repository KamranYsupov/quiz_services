import uuid
from typing import Optional

from pydantic import BaseModel, ConfigDict


class TelegramUserBaseSchema(BaseModel):
    telegram_id: int
    username: Optional[str]
    full_name: str


class TelegramUserSchema(TelegramUserBaseSchema):
    id: uuid.UUID
    quiz_answer: Optional[int] = None


class TelegramUserCreateSchema(TelegramUserBaseSchema):
    pass

