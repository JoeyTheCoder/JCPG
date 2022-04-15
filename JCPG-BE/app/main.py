import numbers
from tokenize import Number
from typing import Optional
from fastapi import FastAPI
from core_logic import pokemon
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemon/{item_id}")
async def getPokemon (item_id):
    response = pokemon.getPokemon(item_id)
    return response