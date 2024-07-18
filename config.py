from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_TYPE_SQLITE: str
    DB_TYPE_POSTGRESQL: str
    DB_ENGINE_SQLITE: str
    DB_ENGINE_POSTGRESQL: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def db_url_sqlite(self):
        return f"{self.DB_TYPE_SQLITE}+{self.DB_ENGINE_SQLITE}:///{self.DB_NAME}"

    @property
    def db_url_postgres(self):
        return (f"{self.DB_TYPE_POSTGRESQL}+{self.DB_ENGINE_POSTGRESQL}://{self.DB_USER}:{self.DB_PASS}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
