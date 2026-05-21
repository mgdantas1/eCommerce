from typing import Annotated
from sqlmodel import select, Session
from fastapi import FastAPI, Depends
from database import create_db, get_session
from contextlib import asynccontextmanager
from routers import users, papeis, produtos, categorias, pedidos, enderecos, pagamentos, avaliacoes, estoque

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(papeis.router)
app.include_router(produtos.router)
app.include_router(categorias.router)
app.include_router(pedidos.router)
app.include_router(enderecos.router)
app.include_router(pagamentos.router)
app.include_router(avaliacoes.router)
app.include_router(estoque.router)
