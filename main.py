import random
import string
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/passhome")
def passGen():
    password = ""
    passwordChar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password =   "".join(random.choice(passwordChar)for char in range(10))
    return password







 