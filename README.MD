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
      - `DB_HOST` - IP адрес сервера с БД
      - `DB_PORT` - порт, на котором работает Postgresql
      - `DB_NAME` - имя БД
      - `DB_USER` - пользовательв БД
      - `DB_PASSWORD` - пароль от БД
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
  
  
 