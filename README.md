
Версия без тестов

stack: django + drf + celery + rabbitmq + docker

Сваггер находится по адрессу '/swagger'

NOTE!
После запуска docker compose необходимо сделать следующее:
    - docker-compose exec app bash
    - python manage.py migrate --run-syncdb