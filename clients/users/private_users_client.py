from typing import TypedDict

from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponseDict(TypedDict):
    user: User

class UpdateUserRequestDict(TypedDict):
    email: str | None
    lastName: str | None
    firstNam: str | None
    middleName: str | None

class PrivateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_users_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_users_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        return self.patch(f"/api/v1/users/{user_id}", json=request)

    def delete_users_api(self,user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")

    def get_users(self,user_id: str) -> GetUserResponseDict:
        response = self.get_users_api(user_id)
        return response.json()


def get_private_users_client(user:AuthenticationUserDict) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))