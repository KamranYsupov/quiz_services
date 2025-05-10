from fastapi import APIRouter

from app.api.v1.endpoints.users import router as users_router
from app.api.v1.endpoints.quiz import router as quiz_router


api_router = APIRouter()
api_router.include_router(users_router)
api_router.include_router(quiz_router)

