from pydantic import Field, PostgresDsn
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
    jaeger_host: str = Field(title='Jaeger хост', default='jaeger')
    jaeger_port: int = Field(title='Jaeger порт', default=6831)

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
    use_sqlite: bool = Field(default=False)

    # endregion

    container_wiring_modules: list = [
        'app.api.v1.endpoints.users',
        'app.api.v1.endpoints.quiz',
        'app.db.transaction'
    ]

    @property
    def db_url(self) -> str:
        if self.use_sqlite:
            return self.sqlite_default_url

        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            path=self.db_name
        ).unicode_string()

    class Config:
        env_file = '.env'


settings = Settings()
