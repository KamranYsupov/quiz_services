import loguru
from aiogram import Router, types
from aiogram.filters import CommandStart
import aiohttp
from aiogram.fsm.context import FSMContext
from dependency_injector.wiring import inject, Provide

from core.container import Container
from opentelemetry import trace
from schemas.user import TelegramUserCreateSchema
from services.quiz_api import QuizAPIV1Service
from states.quiz import QuizState

router = Router()


@router.message(CommandStart())
@inject
async def start_command_handler(
        message: types.Message,
        state: FSMContext,
        quiz_api_v1_service: QuizAPIV1Service = Provide[
            Container.quiz_api_v1_service
        ],
):
    print('start')
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span('start_command') as span:
        print('trace')
        user_data = await quiz_api_v1_service.get_user(
            user_id=message.from_user.id
        )

        if not user_data:
            from_user_data = message.from_user.model_dump()
            from_user_data['telegram_id'] = from_user_data.pop('id')
            from_user_data['full_name'] = message.from_user.full_name

            user_schema = TelegramUserCreateSchema(
            **from_user_data
            )
            user_data = await quiz_api_v1_service.create_user(
                obj=user_schema
            )

        full_name = user_data.get('full_name')
        message_text = (
            f'Привет, {full_name}. '
            'Сыграем в викторину?\n\nОтправь мне любое произвольное число.'
        )
        await message.answer(message_text)
        await state.set_state(QuizState.answer)