
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from LLM_Refinery.core.agent_pipeline import run_pipeline
from uuid import uuid4
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get("/live", response_class=HTMLResponse)
async def live_dashboard(request: Request):
    return templates.TemplateResponse("live_dashboard.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})
from fastapi.responses import RedirectResponse  # Add to your imports if not already

@app.get("/", response_class=HTMLResponse)
def root():
    return RedirectResponse(url="/dashboard")

@app.post("/run_pipeline", response_class=HTMLResponse)
def run_pipeline_htmx(request: Request,
                      prompt: str = Form(...),
                      goal: str = Form(...),
                      tone: str = Form(...),
                      style: str = Form(...),
                      persona: str = Form(...),
                      domain: str = Form(...)):

    user_input = {
        "original_input": prompt,
        "goal": goal,
        "tone": tone,
        "style": style,
        "character": persona,
        "domain": domain
    }

    # Modified pipeline to yield agent name and output at each step
    output_blocks = run_pipeline(user_input, yield_mode=True)

    blocks = ""
    for name, output in output_blocks:
        blocks += f"""
        <div class='agent-output'>
            <h4>{name}</h4>
            <pre>{output}</pre>
        </div>
        """

    return HTMLResponse(blocks)