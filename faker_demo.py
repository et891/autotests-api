from faker import Faker
import httpx

fake = Faker()

# Генерация фейковых данных
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "age": fake.random_int(min=18, max=100)
}

# Отправка POST-запроса с фейковыми данными
response = httpx.post("http://localhost:8000/api/v1/users", json=user_data)

print(response.text)
# Проверка, что запрос прошел успешно
