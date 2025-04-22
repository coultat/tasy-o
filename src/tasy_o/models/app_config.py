from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from tasy_o.api.constants import DEFAULT_ENV_PATH


class AppConfig(BaseSettings):
    name: str = Field(default="fastapi_name", validation_alias="FASTAPI_NAME")
    version: str = Field(default="fastapi_version", validation_alias="FASTAPI_VERSION")
    description: str = Field(
        default="fastapi_description", validation_alias="FASTAPI_DESCRIPTION"
    )
    docs_url: str = Field(
        default="/docs",
        validation_alias="FASTAPI_DOC_URL",
    )
    model_config = SettingsConfigDict(env_file=DEFAULT_ENV_PATH)


app_config = AppConfig()
