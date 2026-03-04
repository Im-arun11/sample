from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.ai_service import analyze_code

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.post("/analyze")
def analyze(request: Request, code: str = Form(...)):
    result = analyze_code(code)

    return result   # 🔥 temporary debug