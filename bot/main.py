import asyncio

import loguru
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

from loader import bot, dp
from handlers.routing import get_main_router
from core.container import Container
from core import config


def set_tracing():
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({SERVICE_NAME: config.SERVICE_NAME})
        )
    )

    jaeger_exporter = JaegerExporter(
        agent_host_name=config.JAEGER_HOST,
        agent_port=config.JAEGER_PORT,
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    return trace


async def main():
    """Запуск бота"""
    dp.include_router(get_main_router())

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    loguru.logger.info('Bot is starting')

    container = Container()
    container.init_resources()
    container.wire(modules=config.CONTAINER_WIRING_MODULES)

    set_tracing()
    asyncio.run(main())