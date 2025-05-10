from dependency_injector import containers, providers

from app.repositories import (
    RepositoryTelegramUser
)
from app.services import (
    TelegramUserService
)
from app.db import DataBaseManager
from app.db.models import TelegramUser
from app.core.config import settings




class Container(containers.DeclarativeContainer):
    db_manager = providers.Singleton(DataBaseManager, db_url=settings.db_url)
    session = providers.Resource(db_manager().get_async_session)

    # region repository
    repository_telegram_user = providers.Singleton(
        RepositoryTelegramUser, model=TelegramUser, session=session
    )
    # endregion

    # region services
    telegram_user_service = providers.Singleton(
        TelegramUserService,
        repository_telegram_user=repository_telegram_user,
        unique_fields=('telegram_id', 'username',)
    )
    # endregion


