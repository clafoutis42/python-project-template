from fastapi import FastAPI

from .routers import health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="{{cookiecutter.project_name}}",
        description="{{cookiecutter.project_description}}",
        version="{{cookiecutter.version}}",
    )
    
    app.include_router(health_router)
    
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)