# Django Demo for Hostim.dev

This is a Django application that demonstrates a user management system with several key features:

## What it does

- Creates and lists users
- Supports avatar image uploads
- Uses MySQL for the database
- Uses Redis for caching
- Runs in Docker containers

## Tech used

- Python with Django 5.2
- MySQL 8.0
- Redis 7
- Docker + Docker Compose
- Django templates

## How it's organized

- `core/models.py` - Defines the UserProfile model
- `core/forms.py` - Contains UserCreationForm for adding users
- `core/views.py` - Includes view functions for user management
- `core/urls.py` - Defines URL routing for the app
- `docker-compose.yml` - Configures three services: web, MySQL, and Redis
- `Dockerfile` - Builds the Django app container

## Key Features

### User Management

The application has a custom user management system that extends Django's built-in User model with a UserProfile model that includes:

- Avatar images (stored in media/avatars/)
- User status tracking

### Caching with Redis

The application uses Redis for caching user data:

- The `user_management` view in `core/views.py` first checks the Redis cache
- If data isn't cached, it pulls from the database and caches it
- The cache is invalidated when new users are added

### Database Integration

The application uses MySQL:

- The app uses MySQL, configured via environment variables (MYSQL\_\*)
- Migrations are automatically applied at container startup

## How to run it

To run the app locally:

```bash
docker-compose up --build
```

Docker Compose sets up three services:

- The web app (Django)
- MySQL
- Redis

The web application will be available at [http://localhost:8000/](http://localhost:8000/)

## Notes

- The application uses Django's built-in User model with a custom UserProfile model
- Avatar images are stored in a persistent volume mounted at `/app/media`
- Database and Redis data are also stored in persistent volumes

This app is also set up for easy deployment on Hostim.dev. It shows how to spin up a full stack app with a database and cache inside containers. For detailed steps on hosting this on Hostim.dev, [check out the Hostim.dev deployment guide](https://hostim.dev/docs/guides/frameworks/django).
