
from fastapi import FastAPI, Request, Depends, BackgroundTasks
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel 
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="C:/Users/yaharin/Downloads/bootstrap-sidebar-04/RuleViewerBasic")
app.mount("/css", StaticFiles(directory="css"), name="static")
app.mount("/js", StaticFiles(directory="js"), name="staticjs")
app.mount("/scss", StaticFiles(directory="scss"), name="staticScss")

@app.get("/")
def about(request: Request):
    return templates.TemplateResponse("form.html", {
        "request" : request
    }) 

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {
        "request" : request
    }) 
