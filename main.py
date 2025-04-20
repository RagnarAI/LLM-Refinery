# main.py (frontend entry point)
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from LLM_Refinery.core.agent_pipeline import run_pipeline
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/config", response_class=HTMLResponse)
def config_page(request: Request):
    return templates.TemplateResponse("config.html", {"request": request})

@app.post("/run", response_class=HTMLResponse)
def run_refinery(
    request: Request,
    original_input: str = Form(...),
    goal: str = Form(...),
    tone: str = Form(...),
    style: str = Form(...),
    character: str = Form(...),
    domain: str = Form(...)
):
    config = {
        "original_input": original_input,
        "goal": goal,
        "tone": tone,
        "style": style,
        "character": character,
        "domain": domain
    }
    response, evaluation, feedback = run_pipeline(config)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "result": response,
        "evaluation": evaluation,
        "feedback": feedback
    })

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
