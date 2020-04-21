from app.core.routers.hello import router as hello_router
from app.core.routers.employee import router as employee_router
from app.core.routers.auth import router as auth_router
from app.utils.api.router import TypedAPIRouter

hello_router = TypedAPIRouter(router=hello_router, prefix="/hello", tags=["Hello"])
employee_router = TypedAPIRouter(router=employee_router, prefix="/employee", tags=["Employee"])
auth_router = TypedAPIRouter(router=auth_router, prefix="/auth", tags=["Authentication"])
