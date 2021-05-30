# Boilerplate Django Independent Backend

The code is based on two main services based on DJANGO (app) and POSTGRESQL (relational db).

## Development Environment

#### Clone the Repository

```
mkdir app
git clone REPO_URL app/
```

#### Adjust Settings

Duplicate .env.sample as .env.docker and setup local details

#### Run Containers Structure

This will include services related to Django and PostgreSQL

```
docker-compose up
```

#### Access Django Container

```
docker-compose exec django sh
```

#### Create Superuser

```
python manage.py createsuperuser
```

#### Makefile

Make commands are available for most of the commands used during development, check Makefile to understand what is there.
