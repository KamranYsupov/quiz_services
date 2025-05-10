import uuid
from typing import Dict, Any

from dependency_injector import providers
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header, HTTPException
from starlette import status

from app.core.container import Container
from app.db.models import TelegramUser
from app.db.transaction import atomic
from app.schemas.user import TelegramCreateUserSchema, TelegramUserSchema
from app.services import TelegramUserService

router = APIRouter(tags=['TelegramUser'], prefix='/telegram_users')


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
async def create_user(
        telegram_user_schema: TelegramCreateUserSchema,
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
    '/{user_id}/',
    status_code=status.HTTP_200_OK,
    response_model_exclude_none=True,
)
@inject
async def get_user(
        user_id: uuid.UUID,
        telegram_user_service: TelegramUserService = Depends(
            Provide[Container.telegram_user_service]
        ),
) -> TelegramUserSchema:
    telegram_user: TelegramUser = await telegram_user_service.get(
        id=user_id
    )
    if not telegram_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    telegram_user_schema = telegram_user.serialize(
        schema_class=TelegramUserSchema,
    )
    return telegram_user_schema


@router.get('/', status_code=status.HTTP_200_OK)
@inject
async def get_user_ids(
        telegram_user_service: TelegramUserService = Depends(
            Provide[Container.telegram_user_service]
        ),
) -> dict:
    telegram_users = await telegram_user_service.list()
    data = {'ids': [telegram_user.id for telegram_user in telegram_users]}

    return data


