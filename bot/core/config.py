import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

API_URL = os.getenv('API_URL', 'http://localhost:8000/api/')
API_V1_URL = os.getenv('API_V1_URL', f'{API_URL}v1/')

CONTAINER_WIRING_MODULES = [
    'handlers.start',
    'handlers.quiz'
]