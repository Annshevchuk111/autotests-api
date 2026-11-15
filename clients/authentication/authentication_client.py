from clients.api_client import APIClient
from clients.authentication.authentication_schema import LoginRequestSchema,LoginResponseSchema,RefreshRequestSchema
from clients.public_http_builder import get_public_http_client
from httpx import Response



class AuthenticationClient(APIClient):
    def login_api(self, request:LoginRequestSchema) -> Response:
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))

    def refresh_api(self, request:RefreshRequestSchema) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        # Инициализируем модель через валидацию JSON строки
        return LoginResponseSchema.model_validate_json(response.text)

def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())

