import os

from celery import Celery

from core import config

app = Celery(
    config.SERVICE_NAME,
    namespace='CELERY',
    backend=config.CELERY_BACKEND_URL,
    broker=config.CELERY_BROKER_URL,
)
app.autodiscover_tasks(['tasks'])

from tasks.quiz import (
    is_number_prime_task
)

