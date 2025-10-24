# HTMX Demo

A comprehensive training resource for teams transitioning from jQuery/AJAX to HTMX, built with Django.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Overview

This project provides side-by-side comparisons of jQuery/AJAX and HTMX implementations for common web interaction patterns. Perfect for research software engineering teams looking to modernize their Django applications.

### What's Included

- **7 Interactive Patterns**: Form submissions, live search, infinite scroll, modals, dynamic lists, dependent dropdowns, and polling
- **Side-by-Side Comparisons**: See jQuery and HTMX implementations together
- **HTMX Deep Dive**: Detailed explanations and best practices
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

## Quick Start

### Option 1: Docker (Recommended for Production-like Setup)

1. **Build the Docker images:**
   ```bash
   docker compose -f docker-compose.local.yml build
   ```

2. **Start the containers:**
   ```bash
   docker compose -f docker-compose.local.yml up -d
   ```

3. **Run migrations and load sample data:**
   ```bash
   docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
   
   # Load curated fixture (recommended for demos)
   docker compose -f docker-compose.local.yml run --rm django python manage.py loaddata sample_data
   
   # OR generate random data (larger dataset)
   docker compose -f docker-compose.local.yml run --rm django python manage.py create_sample_data
   ```

4. **Create a superuser (optional):**
   ```bash
   docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
   ```

### Option 2: Local Development (Faster for Development)

1. **Install uv (if not already installed):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Set up environment variables:**
   ```bash
   export DATABASE_URL="sqlite:///db.sqlite3"
   export DJANGO_DEBUG=True
   export DJANGO_SECRET_KEY="your-secret-key-here"
   ```

4. **Run migrations:**
   ```bash
   uv run python manage.py migrate
   ```

5. **Load sample data:**
   ```bash
   # Option A: Load curated fixture (recommended for demos)
   uv run python manage.py loaddata sample_data
   
   # Option B: Generate random data (larger dataset)
   uv run python manage.py create_sample_data
   ```

6. **Run the development server:**
   ```bash
   uv run python manage.py runserver
   ```

Your application will be running at http://localhost:8000

## Exploring the Examples

Once the server is running, visit:

- **http://localhost:8000/** - Home page with overview
- **http://localhost:8000/examples/** - Examples landing page
- **http://localhost:8000/examples/comparison/** - Side-by-side jQuery vs HTMX comparisons
- **http://localhost:8000/examples/htmx-deep-dive/** - HTMX-focused deep dive with explanations

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
│   ├── static/
│   │   └── css/
│   │       └── examples.css  # Styling for examples
│   └── templates/
│       └── examples/       # All example templates
│           ├── index.html
│           ├── comparison.html
│           ├── htmx_deep_dive.html
│           └── partials/   # HTML fragments for HTMX
└── README.md               # This file
```

## Using for Team Training

### For Instructors

1. Start with the **comparison page** to show side-by-side implementations
2. Open browser DevTools to demonstrate request/response differences
3. Walk through the **code** to explain the patterns
4. Use the **deep dive page** for detailed explanations
5. Reference the **documentation** for comprehensive coverage

### For Learners

1. **Explore** the interactive examples
2. **View page source** to see HTMX attributes in action
3. **Open DevTools Network tab** to observe requests
4. **Read the documentation** to understand concepts
5. **Experiment** with modifications
6. **Apply** patterns to your own projects

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

## Contributing

This project is designed for educational purposes. Feel free to:

- Add new examples
- Improve existing patterns
- Enhance documentation
- Report issues
- Submit pull requests
