from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_TYPE: str
    DB_ENGINE: str
    DB_NAME: str

    @property
    def get_url_db(self):
        return f"{self.DB_TYPE}+{self.DB_ENGINE}:///{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
