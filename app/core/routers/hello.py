from fastapi import APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.core.routers.auth import get_current_username
from starlette.responses import HTMLResponse, JSONResponse

router = APIRouter()
security = HTTPBasic()


@router.get("/get", description="Hello World!", response_description="Some text")
async def get():
    return HTMLResponse("Hello!")

