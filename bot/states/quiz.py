from aiogram.fsm.state import StatesGroup, State


class QuizState(StatesGroup):
    answer: State()