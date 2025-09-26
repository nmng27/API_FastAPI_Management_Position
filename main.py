from fastapi import FastAPI
from services.CreateTables import create_table
app = FastAPI()

@app.post("/create_tables")
def create_tables():
    create_table()
    return {
        "status":"Tabelas Criadas!"
    }