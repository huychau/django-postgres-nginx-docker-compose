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
- Set runner mode
  - **migrate**: migrating data
  - **dev**: running development server
  - **test**: running unittest and test coverage

```
export RUNNER_MODE=migrate|dev|test
```

  *Note: Should add `RUNNER_MODE` is `migrate` in first time.*

- Build 
```
docker-compose build
```

- Run
```
docker-compose run
```

## Open on browser
- API: http://localhost:8000/api/v1
- Test coverage: http://localhost:8080
