from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_origins=["*"],
    allow_methods=["*"]
    
)

@app.middleware("http")

async def ware(requst:Request,next_call):

    response = await next_call(requst)

    return response

@app.get("/hello")

def home():

    return {"hello":"you are right"}