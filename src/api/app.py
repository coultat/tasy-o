from config import create_fastapi_app
from models.app_config import app_config
#from exercises.maths.maths_router import maths_router



fastapi_app = create_fastapi_app(app_config=app_config)
#fastapi_app.include_router(maths_router)

@fastapi_app.get("/test")
async def hello_world():
    return {'result': 'hello_world'}

