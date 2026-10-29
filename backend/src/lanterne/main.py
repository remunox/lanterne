"""
App's main entry point
"""

from fastapi import FastAPI

from lanterne.api import router
from lanterne.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(router, prefix="/api")
