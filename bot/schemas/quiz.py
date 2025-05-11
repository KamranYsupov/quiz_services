from pydantic import BaseModel


class AnswerQuizSchema(BaseModel):
    telegram_id: int
    quiz_answer: int
