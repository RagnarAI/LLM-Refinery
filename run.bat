@echo off
echo Starting LLM Refinery UI on port 8500...
call venv\Scripts\activate.bat
start http://localhost:8500
uvicorn main:app --reload --port 8500
pause
