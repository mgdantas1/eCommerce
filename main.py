from typing import Annotated
from sqlmodel import select, Session
from fastapi import FastAPI, Depends, HTTPException
from database import create_db, get_session
from contextlib import asynccontextmanager
from models import Usuarios, Papeis

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get('/users')
def listar_usuarios(session: SessionDep) -> list[Usuarios]:
    usuarios = session.exec(select(Usuarios)).all()
    return usuarios

@app.post('/users')
def cadastrar_usuarios(session: SessionDep, user: Usuarios) -> Usuarios:
    usuario = session.exec(select(Usuarios).where(Usuarios.email == user.email)).first()
    if not usuario:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    raise HTTPException(status_code=400, detail='Usuário já cadastrado')

@app.put('/users')
def editar_papeis(session: SessionDep, id: int, user: Usuarios) -> Usuarios:
    userUpdate = session.get(Usuarios, id)
    if userUpdate:
        userUpdate.nome = user.nome
        userUpdate.email = user.email
        userUpdate.senha_hash = user.senha_hash
        session.add(userUpdate)
        session.commit()
        session.refresh(userUpdate)
        return userUpdate
    
    raise HTTPException(status_code=400, detail="Usuário não existe")

@app.delete('/users')
def excluir_usuarios(session: SessionDep, id: int):
    usuario = session.get(Usuarios, id)
    if usuario:
        session.delete(usuario)
        session.commit()
        return "Usuário deletado com sucesso"

    raise HTTPException(status_code=400, detail="Usuário não existe")

@app.get('/papeis')
def listar_papeis(session: SessionDep) -> list[Papeis]:
    papeis = session.exec(select(Papeis)).all()
    return papeis

@app.post('/papeis')
def cadastrar_papeis(session: SessionDep, papel: Papeis) -> Papeis:
    session.add(papel)
    session.commit()
    session.refresh(papel)
    return papel
    
@app.put('/papeis')
def editar_papeis(session: SessionDep, id: int, papel: Papeis) -> Papeis:
    papelUpdate = session.get(Papeis, id)
    if papelUpdate:
        papelUpdate.nome = papel.nome
        session.add(papelUpdate)
        session.commit()
        session.refresh(papelUpdate)
        return papelUpdate
    
    raise HTTPException(status_code=400, detail="O papel não existe")

@app.delete('/papeis')
def excluir_papeis(session: SessionDep, id: int):
    papel = session.get(Papeis, id)
    if papel:
        session.delete(papel)
        session.commit()
        return "Papel deletado com sucesso"
    
    raise HTTPException(status_code=400, detail="Papel não existe")