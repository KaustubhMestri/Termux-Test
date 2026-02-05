from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Welcome Web App")

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# GET → show form
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": None}
    )

# POST → handle name & show welcome
@app.post("/", response_class=HTMLResponse)
def welcome(request: Request, name: str = Form(...)):
    message = f"Welcome, {name} 🎉"
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "message": message}
    )
