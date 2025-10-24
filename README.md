# HTMX Demo

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Quickstart

Get up and running in three simple steps:

1. **Build the Docker images:**
   ```bash
   docker compose -f docker-compose.local.yml build
   ```

2. **Start the containers:**
   ```bash
   docker compose -f docker-compose.local.yml up -d
   ```

3. **Create a superuser:**
   ```bash
   docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
   ```

Your application will be running at http://localhost:8000
