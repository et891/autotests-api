import httpx

from tools.fakers import fake

# Создаем пользователя
create_user_payload = {
    "email": fake.email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Получаем данные пользователя
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

put_user_payload = {
  "email": fake.email(),
  "lastName": "string1",
  "firstName": "string1",
  "middleName": "string1"
}

put_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=get_user_headers, json=put_user_payload
)
get_user_response_data = put_user_response.json()
print('Get user data:', get_user_response_data)
