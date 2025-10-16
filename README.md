# Hotel

Django-приложение для управления бронированием номеров, гостями и услугами гостиницы. 

## Начало работы

Эти инструкции предоставят вам копию проекта и помогут запустить на вашем локальном компьютере для разработки и тестирования.

### Необходимые условия

PyCharm
PostgreSQL

### Установка

Запустите PyCharm

Создайте новый проект

Установите django
pip install django psycopg2-binary

Клонируйте репозиторий с git
git clone https://github.com/Minzhy1/Hotel.git

Сделайте миграцию
python manage.py makemigrations
python manage.py migrate

Запустите проект
python manage.py runserver

Для проверки перейдите на запущенный сайт
http://127.0.0.1:8000/

## Авторы

* **Николай Букреев** - - [Minzhy1](https://github.com/Minzhy1)
