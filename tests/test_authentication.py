from http import HTTPStatus
import pytest
from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code, assert_equal
from tools.assertions.schema import validate_json_schema
from tools.assertions.base import assert_is_true

@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    public_users_client=get_public_users_client()

    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code,HTTPStatus.OK)

    private_client = get_authentication_client()
    request_login = LoginRequestSchema(email=request.email,password=request.password)
    response_login = private_client.login_api(request_login)
    response_data_login = LoginResponseSchema.model_validate_json(response_login.text)

    print(response_data_login)
    assert_status_code(response_login.status_code,HTTPStatus.OK)
    assert_equal(response_data_login.token.token_type, expected='bearer',name='token type')
    assert_is_true(response_data_login.token.access_token,"access_token")
    assert_is_true(response_data_login.token.refresh_token, "refresh_token")

    validate_json_schema(response_login.json(), response_data_login.model_json_schema())
