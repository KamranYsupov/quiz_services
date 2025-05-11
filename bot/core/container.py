from dependency_injector import containers, providers

from services.quiz_api import QuizAPIV1Service


class Container(containers.DeclarativeContainer):
    # region services
    quiz_api_v1_service = providers.Singleton(QuizAPIV1Service)
    # endregion
