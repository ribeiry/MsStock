from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

_settings = None


class Environments(BaseModel):
    database_name: str
    root_path: str
    api_url: str
    api_port: str
    db_uri: str
    db_name: str

    @classmethod
    def build(cls, args: dict):
        return Environments(
            database_name=args.get("database_name", ""),
            root_path=args.get("root_path", ""),
            api_url=args.get("api_url", ""),
            api_port=args.get("api_port", ""),
            db_uri=args.get("db_uri", ""),
            db_name=args.get("db_name", ""),
        )


class Settings(BaseSettings):

    api_port: str = Field(alias="API_PORT", default="")
    api_url: str = Field(alias="API_URL", default="")
    root_path: str = Field(alias="ROOT_PATH", default="")
    db_uri: str = Field(alias="DB_URI", default="")
    db_name: str = Field(alias="DB_NAME", default="")
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        case_sensitive=False,
    )

    @classmethod
    def get_settings(cls):
        global _settings

        if _settings is None:
            _settings = Settings()

        return Environments.build(_settings.model_dump())
