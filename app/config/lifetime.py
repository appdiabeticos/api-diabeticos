from typing import Awaitable, Callable
from fastapi import FastAPI


def startup(app: FastAPI) -> Callable[[], Awaitable[None]]:
    async def _startup() -> None:
        pass
    return _startup

def shutdown(app: FastAPI) -> Callable[[], Awaitable[None]]:
    async def _shutdown() -> None:
        pass
    return _shutdown

