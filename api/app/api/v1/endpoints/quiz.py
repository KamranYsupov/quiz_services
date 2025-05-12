from typing import Dict, Any

from dependency_injector import providers
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.core.container import Container
from app.db.models import TelegramUser
from app.db.transaction import atomic
from app.schemas.quiz import AnswerQuizSchema
from app.services import TelegramUserService

router = APIRouter(tags=['Quiz'], prefix='/quizzes')


@router.patch('/answer_quiz', status_code=status.HTTP_200_OK)
@inject
async def answer_quiz(
        answer: AnswerQuizSchema,
        telegram_user_service: TelegramUserService = Depends(
            Provide[Container.telegram_user_service]
        ),
        session: AsyncSession = Depends(
            Provide[Container.session]
        )
) -> dict:
    telegram_user: TelegramUser = await telegram_user_service.get(
        telegram_id=answer.telegram_id
    )
    if not telegram_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='user not found'
        )

    telegram_user.quiz_answer = answer.quiz_answer
    session.add(telegram_user)
    await session.commit()

    return {'status': 'ok'}
