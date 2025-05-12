from aiogram import Router

from .start import router as start_router
from .quiz import router as quiz_router


def get_main_router() -> Router:
    router = Router()

    router.include_routers(
        start_router,
        quiz_router

    )

    return router