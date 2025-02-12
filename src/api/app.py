from config import create_fastapi_app
from models.app_config import app_config


fastapi_app = create_fastapi_app(app_config=app_config)
