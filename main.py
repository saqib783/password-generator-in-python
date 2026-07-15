import secrets
import string
import logging
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static",StaticFiles(directory="frontend_template"),name="static")


@app.get("/" ,response_class=HTMLResponse)
def home():
    with open("frontend_template/index.html","r",encoding="utf-8") as file:
        return  file.read()

class PasswordBase(BaseModel):
    pass_len: int
    special_char: bool


@app.post("/passhome")
def passGen(config:PasswordBase):
    logger = logging.getLogger("uvicorn.error")
    if config.special_char:
        punctuation_list  = ["!","@","#","$","_","-"]
        punctuation_string = "".join(punctuation_list)
        passwordChar = string.ascii_lowercase + string.ascii_uppercase + string.digits + punctuation_string
        password =   "".join(secrets.choice(passwordChar)for char in range(config.pass_len))
    else:
        passwordChar = string.ascii_lowercase + string.ascii_uppercase + string.digits 
        password =   "".join(secrets.choice(passwordChar)for char in range(config.pass_len))
    logger.info(password)
    return {"password": password}


