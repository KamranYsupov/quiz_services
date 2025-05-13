from typing import Optional

from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UUIDMixin, TimestampedMixin


class TelegramUser(Base, UUIDMixin, TimestampedMixin):
    """Модель пользователя"""

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    full_name: Mapped[str]
    quiz_answer: Mapped[Optional[int]] = mapped_column(default=None)

