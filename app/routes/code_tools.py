from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.services.ai_service import refine_code
from app.services.plagiarism_service import check_plagiarism

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/plagiarism", response_class=HTMLResponse)
async def plagiarism(request: Request, code: str = Form(...)):

    percent = check_plagiarism(code)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "code": code,
            "plagiarism": percent
        }
    )


@router.post("/refine", response_class=HTMLResponse)
async def refine(request: Request, code: str = Form(...)):

    new_code = refine_code(code)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "code": code,
            "result": new_code
        }
    )