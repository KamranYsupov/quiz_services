from typing import TYPE_CHECKING, Optional
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UUIDMixin, TimestampedMixin


class TelegramUser(Base, UUIDMixin, TimestampedMixin):
    """Модель пользователя"""

    telegram_id: Mapped[int] = mapped_column(unique=True, index=True)
    username: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    fullname: Mapped[str]

