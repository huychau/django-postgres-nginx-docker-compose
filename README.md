# Practice 2: Docker compose stack
Learn how to use Docker compose syntax and commands.

## Stacks
- Django
- PostgreSQL
- Nginx
- Gunicorn

## Targets:  
Create docker-compose file(s) that satifies the following requirements:

- Compose up a Django app with PostgreSQL as database.
- Serve API via Nginx proxy.
- Have a service to migrate/init data from Django app.
- Have a service to test your Django app.
- Auto-reload Django app whenever a change is made from backend code.
- Persistence the database.

## How to build
- Set environtment mode
  - **dev**: running development server
  - **test**: running unittest and test coverage

```
export ENV=dev|test
```

- Run
```
docker-compose run
```

- Load dump data
```
docker exec -it web ./manage.py loaddata data.json
```

- Collect static files
```
docker exec -it web ./manage.py collectstatic --noinput
```

## Open on browser
- API: http://localhost:8000/api/v1
- Test coverage: http://localhost:8080
