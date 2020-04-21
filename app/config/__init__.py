"""Config of application"""
from app.config.db import TortoiseSettings
from app.config.openapi import OpenAPISettings

tortoise_config = TortoiseSettings.generate()
openapi_config = OpenAPISettings.generate()
