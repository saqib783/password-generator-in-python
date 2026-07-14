import random
import string
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/passhome")
def passGen():
    password = ""
    passwordChar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password =   "".join(random.choice(passwordChar)for char in range(10))
    return password







 