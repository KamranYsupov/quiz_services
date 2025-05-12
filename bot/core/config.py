import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
SERVICE_NAME = os.getenv('SERVICE_NAME', 'bot')

JAEGER_HOST = os.getenv('JAEGER_HOST', 'jaeger')
JAEGER_PORT = os.getenv('JAEGER_PORT', 6831)

API_URL = os.getenv('API_URL', 'http://nginx:80/api/')
API_V1_URL = os.getenv('API_V1_URL', f'{API_URL}v1/')

CONTAINER_WIRING_MODULES = [
    'handlers.start',
    'handlers.quiz'
]

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = str(os.getenv('REDIS_PORT', 6379))

CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_BACKEND_URL =  f'redis://{REDIS_HOST}:{REDIS_PORT}/1'

