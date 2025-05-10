from typing import Optional, Sequence

from app.db.models import TelegramUser
from app.repositories.user import RepositoryTelegramUser
from .base import CRUDBaseService


class TelegramUserService(CRUDBaseService):
    def __init__(
            self,
            repository_telegram_user: RepositoryTelegramUser,
            unique_fields: Optional[Sequence[str]] = None,
    ):
        self._repository_telegram_user = repository_telegram_user
        super().__init__(
            repository=self._repository_telegram_user,
            unique_fields=unique_fields,
        )

