from fastapi import APIRouter

from lanterne.api import health

router = APIRouter()
router.include_router(health.router)

__all__ = ["router"]
