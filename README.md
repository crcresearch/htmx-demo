# HTMX Demo

A comprehensive training resource for teams transitioning from jQuery/AJAX to HTMX, built with Django.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Overview

This project provides side-by-side comparisons of jQuery/AJAX and HTMX implementations for common web interaction patterns. Perfect for research software engineering teams looking to modernize their Django applications.

### What's Included

- **9 Interactive Patterns**: Form submissions, live search, infinite scroll, modals, dynamic lists, dependent dropdowns, polling, interactive maps, and WebSocket notifications
- **Side-by-Side Comparisons**: See jQuery and HTMX implementations together
- **HTMX Deep Dive**: Detailed explanations and best practices
- **Hands-On Exercises**: Practice building real-world features with guided challenges
- **Comprehensive Documentation**: Guides covering concepts, comparisons, and common pitfalls
- **Sample Data**: Pre-populated examples ready to explore

### Patterns Demonstrated

1. **Form Submissions** - Contact form with inline validation and success messages
2. **Live Search/Filtering** - Search contacts with real-time results
3. **Infinite Scroll/Lazy Loading** - Product list with automatic pagination
4. **Modal Dialogs** - Open modals with server-rendered content
5. **Dynamic List Operations** - Todo list with add/remove/toggle functionality
6. **Dependent Dropdowns** - Country → State → City cascading selects
7. **Polling/Auto-refresh** - Live status dashboard with automatic updates
8. **Interactive Maps (Leaflet)** - Filterable location markers with free OpenStreetMap tiles (no API token required)
9. **WebSocket/Real-time Notifications** - Live notifications using WebSockets with HTMX extensions

### Hands-On Exercises

In addition to the interactive examples, the project includes practical exercises organized by difficulty level:

- **Beginner Exercises**: Start your HTMX journey with foundational patterns
- **Intermediate Exercises**: Level up with more complex real-world scenarios
- **Advanced Exercises**: Master advanced techniques and complex integrations

Each exercise provides a prompt, requirements, starter templates, and hints to help you build features hands-on. No answers provided - the goal is learning through experimentation!

## Quick Start

### Environment Setup

The project includes example environment files in `.envs/.local/` that work out of the box for local development:
- `.envs/.local/.django` - Django configuration
- `.envs/.local/.postgres` - PostgreSQL configuration with safe defaults

These files are already in the repository and require no changes for local development. For production deployments, you'll need to create `.envs/.production/` files with your actual secrets (see Production section below).

### Getting Started

1. **Build the Docker images:**
   ```bash
   docker compose -f docker-compose.local.yml build
   ```

2. **Start the containers:**
   ```bash
   docker compose -f docker-compose.local.yml up -d
   ```

3. **Load sample data:**
   ```bash
   # Load curated fixture (recommended for demos)
   docker compose -f docker-compose.local.yml run --rm django python manage.py loaddata sample_data
   
   # OR generate random data (larger dataset)
   docker compose -f docker-compose.local.yml run --rm django python manage.py create_sample_data
   ```

4. **Create a superuser (optional - not required):**
   ```bash
   docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
   ```

Your application will be running at http://localhost:8000

## Exploring the Examples

Once the server is running, visit:

- **http://localhost:8000/** - Home page with overview
- **http://localhost:8000/examples/** - Examples landing page
- **http://localhost:8000/examples/comparison/** - Side-by-side jQuery vs HTMX comparisons
- **http://localhost:8000/examples/htmx-deep-dive/** - HTMX-focused deep dive with explanations
- **http://localhost:8000/exercises/** - Hands-on exercises for practice

## Documentation

Comprehensive guides are available in the `docs/` directory:

- **[HTMX_GUIDE.md](docs/HTMX_GUIDE.md)** - Complete HTMX reference with attributes, patterns, and best practices
- **[COMPARISON_GUIDE.md](docs/COMPARISON_GUIDE.md)** - Detailed code-by-code comparisons with analysis
- **[GOTCHAS.md](docs/GOTCHAS.md)** - Common pitfalls and how to avoid them

## Key Benefits of HTMX

Based on the examples in this project:

- **66% less code** on average compared to jQuery/AJAX
- **Simpler maintenance** - less JavaScript to manage
- **Server-driven UI** - single source of truth
- **Progressive enhancement** - works without JavaScript
- **Better separation of concerns** - HTML for structure, server for logic

## Project Structure

```
htmx-demo/
├── config/                  # Django settings and main URL config
├── docs/                    # Comprehensive documentation
│   ├── HTMX_GUIDE.md
│   ├── COMPARISON_GUIDE.md
│   └── GOTCHAS.md
├── htmx_demo/
│   ├── examples/           # Main examples app
│   │   ├── models.py       # Data models for demonstrations
│   │   ├── views.py        # jQuery and HTMX view implementations
│   │   ├── urls.py         # URL routing
│   │   └── README.md       # Detailed examples documentation
│   ├── exercises/          # Hands-on practice exercises
│   │   ├── views.py        # Exercise content and routing
│   │   └── README.md       # Exercise documentation
│   ├── static/
│   │   └── css/
│   │       ├── project.css   # Global styling
│   │       └── examples.css  # Styling for examples
│   └── templates/
│       ├── examples/       # All example templates
│       │   ├── index.html
│       │   ├── comparison.html
│       │   ├── htmx_deep_dive.html
│       │   └── partials/   # HTML fragments for HTMX
│       └── exercises/      # Exercise templates
└── README.md               # This file
```

## Using for Team Training

### For Instructors

1. Start with the **comparison page** to show side-by-side implementations
2. Open browser DevTools to demonstrate request/response differences
3. Walk through the **code** to explain the patterns
4. Use the **deep dive page** for detailed explanations
5. Assign **exercises** for hands-on practice
6. Reference the **documentation** for comprehensive coverage

### For Learners

1. **Explore** the interactive examples to see patterns in action
2. **View page source** to see HTMX attributes in action
3. **Open DevTools Network tab** to observe requests
4. **Read the documentation** to understand concepts
5. **Complete exercises** to build real-world features
6. **Experiment** with modifications
7. **Apply** patterns to your own projects

## Development

### Running Tests

```bash
# With uv
uv run pytest

# With Docker
docker compose -f docker-compose.local.yml run --rm django pytest
```

### Code Quality

```bash
# Run linter
uv run ruff check .

# Format code
uv run ruff format .

# Type checking
uv run mypy .
```

## Production Deployment

For production deployments, you'll need to create environment files in `.envs/.production/`:

1. **Copy the example files:**
   ```bash
   cp .envs/.production/.django.example .envs/.production/.django
   cp .envs/.production/.postgres.example .envs/.production/.postgres
   ```

2. **Edit `.envs/.production/.django`** with your production settings:
   - Generate a secure `DJANGO_SECRET_KEY` (50+ characters)
   - Set your `DJANGO_ALLOWED_HOSTS`
   - Configure email settings (MAILGUN_API_KEY, etc.)
   - Set a secure, random `DJANGO_ADMIN_URL`

3. **Edit `.envs/.production/.postgres`** with secure database credentials

**Note:** The actual `.django` and `.postgres` files are gitignored and will never be committed. Only the `.example` templates are in the repository. Keep your secrets safe!

## Contributing

This project is designed for educational purposes. Feel free to:

- Add new examples
- Improve existing patterns
- Enhance documentation
- Report issues
- Submit pull requests
