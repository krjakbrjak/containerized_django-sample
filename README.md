# An example of a containerized [Django](https://www.djangoproject.com) app

Django/drf + PostgreSQL + nginx

## Build/Prepare/Run
```
docker-compose up --build
docker-compose exec app python manage.py migrate
echo '{"author":{"name":"a"}, "name":"B"}' | http POST http://localhost:8080/app/books/
```