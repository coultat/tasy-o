from fastapi import FastAPI
from tasy_o.api.models.app_config import AppConfig



def create_fastapi_app(app_config: AppConfig) -> FastAPI:
    app = FastAPI(
        title=app_config.name,
        version=app_config.version,
        description=app_config.description
    )
    return app