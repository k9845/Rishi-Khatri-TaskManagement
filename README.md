## Setting up Local Development

Install [pyenv](https://github.com/pyenv/pyenv) and  [poetry](https://github.com/python-poetry/poetry)

Install python version in `pyproject.toml` which is `3.10`:
```
pyenv install 3.10
```
Install dependencies:
```
poetry install
```
Update dependencies:
```
poetry update
```

Copy .env.sample file to .env and override there.
```
touch .env
cp .env.sample .env
```

## Runing Development Server

```bash
docker compose build
docker compose up
```

### Making new migrations

     $ docker-compose exec web ./manage.py makemigrations

### If there are conflicting migrations (only works if the migrations don't modify the same models)

     $ docker-compose exec web ./manage.py makemigrations_merge

### Applying the last migration files to database

     $ docker-compose exec web ./manage.py migrate

### Accessing python shell

     $ docker-compose exec web ./manage.py shell

### Adding super user

     $ docker-compose exec web ./manage.py createsuperuser
