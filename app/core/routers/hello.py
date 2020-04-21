from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/get", description="Hello World!", response_description="Some text")
async def get():
    return HTMLResponse("<h1>Hello!</h1>")
