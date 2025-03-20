from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.test_plan_routes import router as test_plan_router
from routes.test_suite_routes import router as test_suite_router
import logging


logging.basicConfig(level=logging.DEBUG)
app = FastAPI()

app.include_router(product_router)
app.include_router(test_plan_router)
app.include_router(test_suite_router)


@app.get("/debug-routes")
def debug_routes():
    return {"routes": [route.path for route in app.routes]}
