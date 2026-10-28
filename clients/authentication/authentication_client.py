from typing import TypedDict

from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema,LoginResponseSchema,RefreshRequestSchema
from clients.public_http_builder import get_public_http_client
from httpx import Response

class Token(TypedDict):  # Добавили структуру с токенами аутентификации
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginRequestDict(TypedDict):
    email: str
    password: str


class LoginResponseDict(TypedDict):  # Добавили структуру ответа аутентификации
    token: Token


class RefreshRequestDict(TypedDict):
    refreshToken: str

class AuthenticationClient(APIClient):
    def login_api(self, request:LoginRequestDict) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request:RefreshRequestSchema) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        # Инициализируем модель через валидацию JSON строки
        return response.json()

def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())

