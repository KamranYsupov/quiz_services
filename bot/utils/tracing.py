from functools import wraps
from typing import Union, Callable

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def start_span(func: Callable):
    @wraps
    async def wrapper(*args, **kwargs):
        with tracer.start_as_current_span(func.__name__) as span:
            result = await func(*args, span=span, *kwargs)

        return result

    return wrapper