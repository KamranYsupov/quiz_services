from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки API"""

    api_v1_prefix: str = Field(title='Префикс первой версии API', default='/api/v1')

    # region Jaeger
    service_name: str = Field(
        title='Название сервиса API',
        alias='API_SERVICE_NAME',
        default='fastapi-service',
    )
    jaeger_host: str = Field(title='Jaeger хост', default='localhost')
    jaeger_post: int = Field(title='Jaeger порт', default=6831)

    # endregion

    # region БД
    db_user: str = Field(title='Пользователь БД')
    db_password: str = Field(title='Пароль БД')
    db_host: str = Field(title='Хост БД')
    db_port: int = Field(title='Порт ДБ', default='5432')
    db_name: str = Field(title='Название БД')
    metadata_naming_convention: dict[str, str] = Field(
        default={
            'ix': 'ix_%(column_0_label)s',
            'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
            'ck': 'ck_%(table_name)s_%(constraint_name)s',
            'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
            'pk': 'pk_%(table_name)s'
        })

    sqlite_default_url: str = Field(
        default='sqlite+aiosqlite:///./db.sqlite3'
    )

    # endregion

    container_wiring_modules: list = [
        'app.api.v1.endpoints.users',
        'app.api.v1.endpoints.quiz',
        'app.db.transaction'
    ]

    @property
    def db_url(self) -> str:
        return self.sqlite_default_url

    class Config:
        env_file = '.env'


settings = Settings()
