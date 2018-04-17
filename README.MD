# Веб приложение для бронирования номеров в гостиницах

Приложение (Restfull бэкенд сервер) позволяющее управлять бронированиями номеров в гостиницах.
Реализованный функционал:
  - Restfull API и админ панель для управления номерами, клиентами, бронированиями (доступны CRUD операции)
  - Аутентификация пользователей API 
  - Админ панель доступна по адресу `http://localhost:8000/admin/`
  - Документация по API доступна по адресу `http://localhost:8000/booking_api/`

## Развертывание приложения
  - Развернуть Postgresql
  - [Только для PROD окружения] Установить следующие переменные окружения 
      - `DATABASE_URL` - строка подключения к СУБД в формате URI
      - `DJANGO_SETTINGS_MODULE=my_web_app.settings_prod` - файл конфигурации Django (различные для dev и prod окружения)
  - Клонировать проект `git clone https://github.com/krtvand/django_example.git`
  - Перейти в папку проекта `cd django_example`
  - Создать виртуальное окружение `virtualenv -p /usr/bin/python3 venv`
  - Активировать виртуальное окружение `source venv/bin/activate`
  - Установить необходимые python модули `pip3 install -r requirements.txt`
  - Перейти в каталог с Django приложением `cd my_web_app/`
  - Применить миграции с помощью команды `python3 manage.py migrate`
  - Создать суперпользователя для веб приложения `python3 manage.py createsuperuser`
  - [Опионально] запустить приложение `python3 manage.py runserver 0:8000`
  
  
 ## Развертываение в Docker
 ```
docker build -t django_example .

docker run -d --name django -p 8000:8000  \
    -e DJANGO_SETTINGS_MODULE=my_web_app.settings_prod \
    -e DATABASE_URL=postgres://user:password@hostname:5432/django_example \
    --restart=always django_example

```
 