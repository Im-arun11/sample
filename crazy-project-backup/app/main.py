from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import home, ai   # importing routers

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(home.router)
app.include_router(ai.router)