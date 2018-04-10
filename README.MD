## Развертывание приложения
  - Развернуть Postgresql
  - Установить следующие переменные окружения 
      - `DB_HOST` - IP адрес сервера с БД
      - `DB_PORT` - порт, на котором работает Postgresql
      - `DB_NAME` - имя БД
      - `DB_USER` - пользовательв БД
      - `DB_PASSWORD` - пароль от БД
  - Клонировать проект `git clone https://github.com/krtvand/django_example.git`
  - Перейти в папку проекта `cd django_example`
  - Создать виртуальное окружение `virtualenv -p /usr/bin/python3 venv`
  - Активировать виртуальное окружение `source venv/bin/activate`
  - Установить необходимые python модули ``
  - Применить миграции с помощью команды `python3 manage.py migrate`
  
  
 