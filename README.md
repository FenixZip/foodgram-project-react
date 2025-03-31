
# 🍲 Продуктовый помощник — Foodgram


---

## 📌 Описание

**Foodgram** — это сервис, где пользователи могут:

- публиковать рецепты;
- добавлять рецепты в избранное;
- подписываться на других авторов;
- формировать список покупок;
- выгружать `.txt` файл с ингредиентами и количеством для блюд.

---

## 🚀 Быстрый старт

### 🧩 Установка

```bash
git clone <project>
cd foodgram-project-react/infra/
cp .env.example .env
```

### 🐳 Запуск в Docker (production)

```bash
sudo docker compose -f docker-compose.production.yml up -d
# или с пересборкой
sudo docker compose -f docker-compose.production.yml up -d --build
```

### ⚙️ Первичная настройка

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic --noinput
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_tags
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_ingredients
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser

# Заливка тестовых данных
sudo docker compose -f docker-compose.production.yml exec backend python manage.py data_test
```

---

## 👤 Тестовые учётные записи

> ⚠️ Актуально, если выполнены все импорты в БД

### 🔐 Админ-зона
- 📍 https://foodgram-ya.ddns.net/admin
- ✉️ Email: fenix15@inbox.ru
- 👤 Логин: fenixzip
- 🔑 Пароль: 123qwerty321

### 👤 Тестовый пользователь
- 📍 http://localhost:8000
- ✉️ Email: fenixzip@yandex.ru
- 🔑 Пароль: 123qwerty321

---

## 📫 Postman и API

### 🔑 Получить токен (тестовый пользователь)

`POST http://localhost/api/auth/token/login/`

```json
{
  "email": "fenixzip@yandex.ru",
  "password": "123qwerty321"
}
```

### 🆕 Регистрация нового пользователя

`POST http://foodgram-ya.ddns.net/api/users/`

```json
{
  "email": "fenixzip@yandex.ru",
  "username": "User101",
  "first_name": "Вася",
  "last_name": "Иванов",
  "password": "Qwerty777"
}
```

### 🔐 Получить токен

`POST http://foodgram-ya.ddns.net/api/auth/token/login/`

```json
{
  "email": "abcde@yandex.ru",
  "password": "Qwerty777"
}
```

✅ Ответ:
```json
{
  "token": "eyJ0e..........."
}
```

🔧 Использование токена в Postman:
- Headers:
  - Key: `Authorization`
  - Value: `Token ваш_токен`

---

## 🛠️ Используемые технологии

- Python 3.11
- Django 5+
- Django REST Framework 3.13
- Postgresql
- Docker, Docker Compose
- Nginx
- GitHub Actions (CI/CD)

---

## 📸 Превью

<img src="https://github.com/HelloAgni/foodgram-project-react/blob/master/backend/media/recipes/images/preview.jpg" alt="preview" width="600" height="350">
