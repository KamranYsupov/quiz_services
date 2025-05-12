import loguru
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from app.api.v1 import routers
from app.core.config import settings
from app.core.container import Container


def set_tracing(fastapi_app: FastAPI):
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create(
                {SERVICE_NAME: settings.service_name}
            ))
    )
    jaeger_exporter = JaegerExporter(
        agent_host_name=settings.jaeger_host,
        agent_port=settings.jaeger_port,
    )
    span_processor = BatchSpanProcessor(jaeger_exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    FastAPIInstrumentor.instrument_app(fastapi_app)


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        title=settings.service_name,
        default_response_class=ORJSONResponse,
    )
    container = Container()
    container.init_resources()
    container.wire(modules=settings.container_wiring_modules)
    fastapi_app.container = container

    fastapi_app.include_router(routers.api_router, prefix=settings.api_v1_prefix)

    set_tracing(fastapi_app)

    return fastapi_app

app = create_app()

if __name__ == '__main__':
    uvicorn.run(app='app.main:app', host='0.0.0.0', reload=True)