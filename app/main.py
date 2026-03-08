from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import code_tools

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.include_router(code_tools.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})