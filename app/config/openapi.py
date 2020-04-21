"""OpenAPI-schema"""
from app.config.base import BaseSettings

OPENAPI_API_NAME = "FastAPI with Postgres Tortoise ORM"
OPENAPI_API_VERSION = "0.0.1 beta"
OPENAPI_API_DESCRIPTION = "API for data handling"


class OpenAPISettings(BaseSettings):
    name: str
    version: str
    description: str

    @classmethod
    def generate(cls):
        return OpenAPISettings(
            name=OPENAPI_API_NAME,
            version=OPENAPI_API_VERSION,
            description=OPENAPI_API_DESCRIPTION,
        )
