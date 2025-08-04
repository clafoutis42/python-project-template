from fastapi import APIRouter

health_router = APIRouter(prefix="/health")


@health_router.get("/")
async def health_check() -> dict[str, str]:
    """Healthcheck Endpoint"""
    return {"status": "OK"}
