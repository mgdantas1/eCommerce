from database import get_session
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Session, select
from models import Usuario

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def listar(session: SessionDep) -> list[Usuario]:
    usuarios = session.exec(select(Usuario)).all()
    return usuarios

@router.post('/')
def cadastrar_usuarios(session: SessionDep, user: Usuario) -> Usuario:
    usuario = session.exec(
        select(Usuario).where(Usuario.email == user.email)
    ).first()

    if not usuario:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    raise HTTPException(status_code=400, detail='Usuário já cadastrado')

@router.put('/{id}')
def editar(session: SessionDep, id: int, user: Usuario) -> Usuario:
    userUpdate = session.get(Usuario, id)

    if userUpdate:
        userUpdate.nome = user.nome
        userUpdate.email = user.email
        userUpdate.senha_hash = user.senha_hash

        session.add(userUpdate)
        session.commit()
        session.refresh(userUpdate)

        return userUpdate

    raise HTTPException(status_code=400, detail="Usuário não existe")

@router.delete('/{id}')
def deletar(session: SessionDep, id: int) -> str:
    usuario = session.get(Usuario, id)

    if usuario:
        session.delete(usuario)
        session.commit()
        return "Usuário deletado com sucesso"

    raise HTTPException(status_code=400, detail="Usuário não existe")