from typing import Dict

import aiohttp

from core import config
from schemas.quiz import AnswerQuizSchema
from schemas.user import (
    TelegramUserSchema,
    TelegramUserCreateSchema,
)
from utils.api import get_response_data_or_raise_exception


class QuizAPIV1Service:
    def __init__(
            self,
            api_url: str = config.API_V1_URL
    ):
        self.api_url = api_url


    async def create_user(
            self,
            obj: TelegramUserCreateSchema
    ) -> Dict:
        url = f'{self.api_url}telegram_users/'
        obj_data = obj.model_dump()

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=obj_data) as response:
                return await get_response_data_or_raise_exception(
                    response=response,
                )

    async def get_user(
            self,
            user_id: str,
    ) -> Dict:
        url = f'{self.api_url}telegram_users/{user_id}/'

        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                return await get_response_data_or_raise_exception(
                    response=response,
                )

    async def answer_quiz(
            self,
            obj: AnswerQuizSchema,
    ) -> Dict:
        url = f'{self.api_url}quizzes/answer_quiz/'
        obj_data = obj.model_dump()

        async with aiohttp.ClientSession() as session:
            async with session.post(url=url, json=obj_data) as response:
                return await get_response_data_or_raise_exception(
                    response=response,
                )
