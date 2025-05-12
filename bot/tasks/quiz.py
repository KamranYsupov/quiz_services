import asyncio
from typing import Union

from celery import shared_task

from utils.number import is_number_prime

from services.telegram import telegram_service


@shared_task
def is_number_prime_task(
        answer: int,
        chat_id: Union[int, str],
) -> None:
    """
    Задача, проверяющая является ли число простым,
    и отправляющая результат викторины пользователю через telegram-бот
    """
    message_text = 'Результат: <tg-spoiler><b>ты {result}</b></tg-spoiler>'

    result = 'победил в викторине!' \
        if is_number_prime(answer) else 'проиграл('

    telegram_service.send_message(
        chat_id=chat_id,
        text=message_text.format(result=result),
    )
