from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyctuator.pyctuator import Pyctuator
import uvicorn

from app.utils.setting import Settings

settings = Settings.get_settings()

API_VERSION = "v1"


tags_metadata = [
    {"name": "Stock"},
]


app = FastAPI()


app = FastAPI(
    title="Service Stock Swagger API (Developer)",
    description="API as a service for service stock",
    version=API_VERSION,
    debug=True,
    root_path=f"/{settings.root_path}",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Healthcheck
pyctuator = Pyctuator(
    app,
    "Monitoring Stock service",
    app_url="http://localhost:8000",
    pyctuator_endpoint_url="http://localhost:8000/pyctuator",
    registration_url="",
)

##app.include_router(book_router, tags=["Stock"], prefix="/stock")

if __name__ == "__main__":
    params = {"host": settings.api_url, "port": int(settings.api_port)}
    uvicorn.run(app, **params)
