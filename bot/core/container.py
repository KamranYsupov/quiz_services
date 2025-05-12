from dependency_injector import containers, providers

from services.quiz_api import QuizAPIV1Service
from services.telegram import TelegramService


class Container(containers.DeclarativeContainer):
    # region services
    quiz_api_v1_service = providers.Singleton(QuizAPIV1Service)
    telegram_service = providers.Singleton(TelegramService)
    # endregion
