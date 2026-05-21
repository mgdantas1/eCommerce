from database import get_session
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Session, select
from models import Produto

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def listar_usuarios(session: SessionDep) -> list[Produto]:
    usuarios = session.exec(select(Produto)).all()
    return usuarios

@router.post('/')
def cadastrar_usuarios(session: SessionDep, user: Produto) -> Produto:
    usuario = session.exec(
        select(Produto).where(Produto.email == user.email)
    ).first()

    if not usuario:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    raise HTTPException(status_code=400, detail='Usuário já cadastrado')

@router.put('/{id}')
def editar_usuarios(session: SessionDep, id: int, user: Produto) -> Produto:
    userUpdate = session.get(Produto, id)

    if userUpdate:
        userUpdate.sqlmodel_update(user.model_dump(exclude_unset=True))
        session.add(userUpdate)
        session.commit()
        session.refresh(userUpdate)

        return userUpdate

    raise HTTPException(status_code=400, detail="Usuário não existe")

@router.delete('/{id}')
def deletar_usuarios(session: SessionDep, id: int) -> str:
    usuario = session.get(Produto, id)
    if usuario:
        session.delete(usuario)
        session.commit()
        return "Usuário deletado com sucesso"

    raise HTTPException(status_code=400, detail="Usuário não existe")