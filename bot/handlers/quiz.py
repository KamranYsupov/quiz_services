import loguru
from aiogram import Router, types, F
from aiogram.filters import CommandStart, StateFilter
import aiohttp
from aiogram.fsm.context import FSMContext
from dependency_injector.wiring import inject, Provide

from core.container import Container
from opentelemetry import trace
from services.quiz_api import QuizAPIV1Service
from states.quiz import QuizState
from schemas.quiz import AnswerQuizSchema
from tasks.quiz import is_number_prime_task

router = Router()


@router.message(F.text, StateFilter(QuizState.answer))
@inject
async def answer_quiz_handler(
        message: types.Message,
        state: FSMContext,
        quiz_api_v1_service: QuizAPIV1Service = Provide[
            Container.quiz_api_v1_service
        ],
):
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span('answer_quiz') as span:
        try:
            answer = int(message.text)
        except ValueError:
            await message.answer(
               'Пожалуйста, отправь целочисленное число.'
            )
            return


        answer_schema = AnswerQuizSchema(
            telegram_id=message.from_user.id,
            quiz_answer=answer,
        )
        await quiz_api_v1_service.answer_quiz(
            obj=answer_schema
        )
        await is_number_prime_task(
            answer=answer,
            chat_id=message.from_user.id,
        )

        await message.answer('Подвожу результаты. . .')
        await state.clear()