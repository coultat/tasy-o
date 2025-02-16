from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from tasy_o.api.constants import DEFAULT_ENV_PATH


class AppConfig(BaseSettings):
    name: str = Field(validation_alias='FASTAPI_NAME')
    version: str = Field(validation_alias='FASTAPI_VERSION')
    description: str = Field(validation_alias="FASTAPI_DESCRIPTION")
    model_config = SettingsConfigDict(env_file=DEFAULT_ENV_PATH)

app_config = AppConfig()