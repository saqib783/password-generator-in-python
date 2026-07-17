import secrets
import string
from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
import redis



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static",StaticFiles(directory="frontend_template"),name="static")
r = redis.Redis(host='localhost',port=6379 , decode_responses= True)





@app.get("/" ,response_class=HTMLResponse)
def home():
    with open("frontend_template/index.html","r",encoding="utf-8") as file:
        return  file.read()

class PasswordBase(BaseModel):
    pass_len: int = 10
    special_char: bool


@app.post("/passhome")
def passGen(config:PasswordBase):
    if config.pass_len > 32 or config.pass_len < 6:
        return {"password": "Error: Length must be between 6 and 32!"}
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    safe_punctuation = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    base_char = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digit)
    ]
    if config.special_char:
        base_password = lower + upper + digit + safe_punctuation
        base_char.append(secrets.choice(safe_punctuation))
    else:
        base_password = lower + upper + digit
    
    remaining_length = config.pass_len - len(base_char)
    remaining_pass = [secrets.choice(base_password) for i in range(remaining_length)]
    password_list = remaining_pass + base_char
    secrets.SystemRandom().shuffle(password_list)
    full_password = "".join(password_list)
    return {"password": full_password}

