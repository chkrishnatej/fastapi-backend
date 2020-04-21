from fastapi import Depends, APIRouter
from app.utils.auth import get_current_username

router = APIRouter()


@router.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username, 'is_secure': True}
