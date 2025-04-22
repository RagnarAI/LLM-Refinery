from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from LLM_Refinery.core.agent_pipeline import run_pipeline
from uuid import uuid4

app = FastAPI()

# Mount static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# === ROUTES ===

# Redirect root to dashboard
@app.get("/", response_class=HTMLResponse)
def root():
    return RedirectResponse(url="/dashboard")

# Main dashboard view (includes result section)
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Config input form page
@app.get("/config", response_class=HTMLResponse)
async def configure(request: Request):
    return templates.TemplateResponse("configure.html", {"request": request})

# Pipeline runner that streams agent-by-agent blocks via HTMX
@app.post("/run_pipeline", response_class=HTMLResponse)
async def run_pipeline_htmx(request: Request,
                            original_input: str = Form(...),
                            goal: str = Form(...),
                            tone: str = Form(...),
                            style: str = Form(...),
                            character: str = Form(...),
                            domain: str = Form(...)):

    # User input passed to the AI agent pipeline
    user_input = {
        "original_input": original_input,
        "goal": goal,
        "tone": tone,
        "style": style,
        "character": character,
        "domain": domain
    }

    # Stream pipeline results one agent at a time (yield_mode must be supported in pipeline)
    output_blocks = run_pipeline(user_input, yield_mode=True)

    # HTML chunk to update inside the dashboard
    blocks = ""
    for name, output in output_blocks:
        blocks += f"""
        <div class='agent-output'>
            <h4>{name}</h4>
            <pre>{output}</pre>
        </div>
        """

    return HTMLResponse(content=blocks)
