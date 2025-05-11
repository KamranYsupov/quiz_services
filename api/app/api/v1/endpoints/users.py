import uuid
from typing import Dict, Any

from dependency_injector import providers
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header, HTTPException
from starlette import status

from app.core.container import Container
from app.db.models import TelegramUser
from app.db.transaction import atomic
from app.schemas.user import TelegramUserCreateSchema, TelegramUserSchema
from app.services import TelegramUserService

router = APIRouter(tags=['TelegramUser'], prefix='/telegram_users')


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def create_user(
        telegram_user_schema: TelegramUserCreateSchema,
        telegram_user_service: TelegramUserService = Depends(
            Provide[Container.telegram_user_service]
        ),
) -> TelegramUserSchema:
    telegram_user: TelegramUser = await telegram_user_service.create(
        obj_in=telegram_user_schema
    )
    telegram_user_schema = telegram_user.serialize(
        schema_class=TelegramUserSchema,
        exclude_fields=('quiz_answer', )
    )
    return telegram_user_schema


@router.get(
    '/{telegram_id}/',
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
@inject
async def get_user(
        telegram_id: int,
        telegram_user_service: TelegramUserService = Depends(
            Provide[Container.telegram_user_service]
        ),
) -> TelegramUserSchema:
    telegram_user: TelegramUser = await telegram_user_service.get(
        telegram_id=telegram_id
    )
    if not telegram_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    telegram_user_schema = telegram_user.serialize(
        schema_class=TelegramUserSchema,
    )
    return telegram_user_schema




