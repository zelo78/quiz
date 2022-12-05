

## Запуск

* Скопируйте файл `.env.example` как `.env` и внесите в него Ваши актуальные данные

```shell
cp .env.example .env
```

### Вариант 1. Запуск в Докере

```shell
docker-compose up -d
```

Создайте администратора
```shell
docker exec -it quiz_app python /app/manage.py createsuperuser
```

Сайт доступен по [адресу http://0.0.0.0:8000](http://0.0.0.0:8000), [панель администрирования](http://0.0.0.0:8000/admin/)

### Вариант 2. Запуск без докера

* Подготовка 

```shell
python3 -m venv venv
source ./venv/bin/activate
```

* Установка зависимостей и подготовка БД
```shell
pip -Ur install src/requirements.txt
python src/manage.py migrate --noinput
python src/manage.py collectstatic --noinput
```

* Создание суперпользователя
```shell
python src/manage.py createsuperuser
```

* Запуск
```shell
python src/manage.py runserver
```

Сайт доступен по [адресу http://127.0.0.1:8000](http://127.0.0.1:8000), [панель администрирования](http://127.0.0.1:8000/admin/)
