# FastAPI Cookiecutter Template

A modern, production-ready cookiecutter template for FastAPI projects.

## Features

- 🚀 **FastAPI** with modern Python features
- 🧪 **Testing** with pytest and coverage reporting  
- 🔧 **Code Quality** with ruff (formatting + linting)
- 📦 **Dependency Management** with uv
- 🐳 **Docker** support (optional)
- 🔄 **CI/CD** with GitHub Actions (optional)
- 🪝 **Pre-commit hooks** (optional)
- 📁 **Clean Architecture** with separation of concerns

## Requirements

- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended) or Python 3.11+

## Quick Start

### 1. Generate a new project

```bash
cookiecutter https://github.com/clafoutis42/python-project-template
```

Or if you have this template locally:

```bash
cookiecutter ./python-project-template
```

### 2. Configure your project

You'll be prompted to configure your project:

```
project_name [My FastAPI Project]: 
project_slug [my-fastapi-project]: 
project_description [A FastAPI project generated from cookiecutter template]: 
author_name [Your Name]: 
author_email [your.email@example.com]: 
version [0.1.0]: 
python_version [~=3.12]: 
include_docker [y]: 
include_github_actions [y]: 
include_pre_commit [y]: 
```

### 3. Set up your new project

```bash
cd your-project-name
uv sync
uv run poe dev
```

Your API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

## Configuration Options

- **project_name**: Human-readable project name (e.g., "My Awesome API")
- **project_slug**: Python package name and directory name (auto-generated from project_name)
- **project_description**: Brief description of your project
- **author_name**: Your full name
- **author_email**: Your email address
- **version**: Initial version (follows semantic versioning)
- **python_version**: Python version constraint for the project
- **include_docker**: Include Docker configuration files
- **include_github_actions**: Include GitHub Actions CI/CD workflow
- **include_pre_commit**: Include pre-commit configuration

## Generated Project Structure

```
your-project/
├── your_project/                    # Main application package
│   ├── __init__.py
│   ├── application/                 # Business logic layer
│   │   ├── __init__.py
│   │   └── exceptions.py           # Application exceptions
│   └── presentation/               # Presentation layer
│       ├── __init__.py
│       └── api/                    # REST API
│           ├── __init__.py
│           ├── main.py            # FastAPI application
│           └── routers/           # API route modules
│               ├── __init__.py
│               └── health.py      # Health check endpoint
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── conftest.py               # Pytest configuration
│   └── presentation/
│       └── api/
│           ├── __init__.py
│           └── test_health.py    # Health endpoint tests
├── .gitignore                     # Git ignore rules
├── .pre-commit-config.yaml       # Pre-commit hooks (optional)
├── .python-version               # Fixed python version for pyenv
├── docker-compose.yml            # Docker Compose config (optional)
├── Dockerfile                    # Docker configuration (optional)
├── example.env                   # Environment variables template
├── pyproject.toml               # Project configuration and dependencies
└── README.md                    # Project documentation
```

## Development Commands

The generated project includes these poethepoet tasks:

```bash
# Development
uv run poe dev          # Start development server with hot reload

# Testing  
uv run poe test         # Run tests
uv run poe test-cov     # Run tests with coverage
uv run poe cov          # Generate coverage report

# Code Quality
uv run poe format       # Format code with ruff
uv run poe lint         # Lint code with ruff
uv run poe ci           # Run all checks (lint + test + coverage)

# Docker (if enabled)
uv run poe build-image  # Build Docker image
```

## Architecture

The template follows a clean architecture pattern:

- **Presentation Layer** (`presentation/`): FastAPI routers, request/response models, API-specific logic
- **Application Layer** (`application/`): Business logic, use cases, application services
- **Domain Layer** (for larger projects): Domain models, business rules, domain services
- **Infrastructure Layer** (for larger projects): External services, database, message queues

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
