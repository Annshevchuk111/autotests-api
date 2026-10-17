import httpx

login_payload = {  "email": "alex11@example.com", "password": "34544"}

login_response= httpx.post(
    "http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response_data)

me_payload = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
me_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=me_payload)
print(me_response.json())