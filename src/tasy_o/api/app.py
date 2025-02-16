from tasy_o.api.config import create_fastapi_app
from tasy_o.api.models.app_config import app_config
from tasy_o.exercises.maths.maths_router import maths_router
import uvicorn

fastapi_app = create_fastapi_app(app_config=app_config)
fastapi_app.include_router(maths_router)

@fastapi_app.get("/hello_world")
async def hello_world():
    return {'result': 'hello_world'}


if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="127.0.0.25", port=8085)