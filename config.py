from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_TYPE: str
    DB_ENGINE: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    @property
    def db_url(self):
        return f"{self.DB_TYPE}+{self.DB_ENGINE}:///{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
