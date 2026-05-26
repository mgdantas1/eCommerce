from fastapi import FastAPI
from routers import papeis, usuarios

app = FastAPI()
app.include_router(usuarios.router)
# app.include_router(papeis.router)c
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)