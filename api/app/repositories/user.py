from .base import RepositoryBase
from app.db.models import TelegramUser


class RepositoryTelegramUser(RepositoryBase[TelegramUser]):
    """Репозиторий для работы с таблицей telegram_users"""
    pass
