import socket

from fastapi import APIRouter

from settings import settings

info_router = APIRouter()


@info_router.get("/backend", tags=["info"], summary="Get the current backend hostname")
async def get_backend():
    return {
        "backend": socket.gethostname()
    }


@info_router.get("/database_host", tags=["info"], summary="Get the current database hostname")
async def get_database_hostname():
    return settings.PGHOST
