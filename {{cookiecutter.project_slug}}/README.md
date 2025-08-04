# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Development

### Setup local environment

Make sure you have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

```sh
# Install dependencies
uv sync

# Run the development server
uv run poe dev
```

The API will be available at `http://localhost:8000`.

### API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

### Testing

```sh
# Run tests
uv run poe test

# Run tests with coverage
uv run poe test-cov

# Generate coverage report
uv run poe cov
```

### Code Quality

```sh
# Format code
uv run poe format

# Run linting
uv run poe lint

# Run all checks (lint + test + coverage)
uv run poe ci
```

{% if cookiecutter.include_docker == 'y' -%}
### Docker

Build the development image:
```sh
docker build -t {{cookiecutter.project_slug}}-development --target development .
```

Build the production image:
```sh
docker build -t {{cookiecutter.project_slug}}-production .
```

Run with docker-compose:
```sh
docker-compose up -d
```
{% endif -%}

## Project Structure

```
{{cookiecutter.project_slug}}/
├── {{cookiecutter.project_slug}}/        # Main application package
│   ├── application/        # Application logic and exceptions
│   │   └── exceptions.py
│   └── presentation/       # API layer
│       └── api/
│           ├── main.py    # FastAPI application
│           └── routers/   # API routes
│               └── health.py
└── tests/                  # Test suite
    └── presentation/
        └── api/
            └── test_health.py
```

{% if cookiecutter.include_pre_commit == 'y' -%}
## Pre-commit Hooks

This project uses pre-commit hooks for code quality. Install them with:

```sh
uv run pre-commit install
```
{% endif -%}

## Environment Variables

Copy `example.env` to `.env` and customize the variables as needed.

```sh
cp example.env .env
```