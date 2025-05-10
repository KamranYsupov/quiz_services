import loguru
from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def start_command_handler(
        message: types.Message,
):
    await message.answer('hi')