import socket

from fastapi import APIRouter

info_router = APIRouter()


@info_router.get("/backend", tags=["info"], summary="Get the current backend hostname")
async def get_backend():
    return {
        "backend": socket.gethostname()
    }
