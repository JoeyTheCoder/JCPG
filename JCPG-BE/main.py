from typing import Optional
from core_logic import pokemon
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/pokemon")
def getPokemon():
    response = pokemon.getPokemon()
    return response