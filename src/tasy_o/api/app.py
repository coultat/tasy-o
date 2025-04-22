from tasy_o.api.config import create_fastapi_app
from tasy_o.models.app_config import app_config
from tasy_o.exercises.maths.maths_router import maths_router


fastapi_app = create_fastapi_app(app_config=app_config)
fastapi_app.include_router(maths_router)


@fastapi_app.get("/hello_world")
async def hello_world():
    return {"result": "hello_world"}
