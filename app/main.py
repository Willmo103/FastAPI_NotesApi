from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates =Jinja2Templates(directory=("templates"))
# templates = Jinja2Templates()

# @app.get("/home", response_model=HTMLResponse)
# def home_page(request: Request):



