 ## Продуктовый помощник - foodgram

 ![workflow](https://github.com/HelloAgni/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

---

 Приложение, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «cписок покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд. Есть возможность выгрузить файл (.txt) с перечнем и количеством необходимых ингредиентов для рецептов.

 ***Для работы с проектом необходимо выполнить действия, описанные ниже.***

 ```bash
git clone <project>
cd foodgram-project-react/infra/
# сделайте копию файла <.env.example> в <.env>
cp .env.example .env
 ```

**Docker**
 ```bash
sudo docker compose -f docker-compose.production.yml up -d
sudo docker compose -f docker-compose.production.yml exec backend python manage.py makemigrations 
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic --noinput
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_tags
sudo docker compose -f docker-compose.production.yml exec backend python manage.py import_ingredients
sudo docker compose -f docker-compose.production.yml exec backend python manage.py createsuperuser
# Для заполнения базы пользователями и рецептами выполните:
sudo docker compose -f docker-compose.production.yml exec backend python manage.py data_test
```
***Тестовый пользователь и администратор***

Если выполнены все импорты в базу данных:
```bash
# Админ зона
http://localhost:8000/admin
Email: fenix15@inbox.ru
Login: fenixzip
Password: 123qwerty321

# Тестовый пользователь
http://localhost:8000
Email: fenixzip@yandex.ru
Password: 123qwerty321

# Документация
http://localhost/redoc
```
**POSTMAN**  
Для полноценного использования API необходимо выполнить регистрацию пользователя и получить токен. Инструкция для ***Postman:***

Получить токен для тестового пользователя если выполнены все импорты:  
POST http://localhost/api/auth/token/login/
```json
{
    "email": "fenixzip@yandex.ru",
    "password": "123qwerty321"
}
```
Без импортов, регистрируем нового пользователя  
POST http://localhost/api/users/
```json
{
    "email": "fenixzip@yandex.ru",
    "username": "User101",
    "first_name": "Вася",
    "last_name": "Иванов",
    "password": "Qwerty777"
}
```
Получаем токен  
POST http://localhost/api/auth/token/login/
```json
{
    "password": "Qwerty777",
    "email": "abcde@yandex.ru"
}
```
Response status 200 OK ✅
```json
{
    "token": "eyJ0e..........."
}
```
Полученный токен вставляем Postman -> закладка Headers -> Key(Authorization) -> Value (Ваш токен в формате: Token da6ee....)  

***Технологии:***  
Python 3.9, Django 3.2, DRF 3.13, Nginx, Docker, Docker-compose, Postgresql, Github Actions.  
<!-- 
***Cервер:***  
http://foodgram-ya.ddns.net/recipes-->

***Превью***  
<img src="https://github.com/HelloAgni/foodgram-project-react/blob/master/backend/media/recipes/images/preview.jpg" alt="img" width="600" height='350'>
