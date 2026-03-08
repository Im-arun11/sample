from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from app.services.ai_service import refine_code
from app.services.plagiarism_service import check_plagiarism

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.post("/process")
def process(request: Request, code: str = Form(...), action: str = Form(...)):
    if action == "refine":
        refined = refine_code(code)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "refined_code": refined, "code": code}
        )
    elif action == "plagiarism":
        result = check_plagiarism(code)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "plagiarism_result": result, "code": code}
        )
    else:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": "Invalid action", "code": code}
        )