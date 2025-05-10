from aiogram import Router

from .start import router as start_router


def get_main_router() -> Router:
    router = Router()

    router.include_routers(
        start_router
    )

    return router