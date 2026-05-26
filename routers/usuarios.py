from database.database import get_session
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlmodel import Session, select
from models.models import Usuarios

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def listar_usuarios(session: SessionDep) -> list[Usuarios]:
    usuarios = session.exec(select(Usuarios)).all()
    return usuarios

@router.get("/{id}")
def listar_usuario_id(session: SessionDep, id: int) -> Usuarios:
    user = session.get(Usuarios, id)
    if not user:
        raise HTTPException(status_code=400, detail="O usuário não existe") 
    return user

@router.post('/')
def cadastrar_usuarios(session: SessionDep, user: Usuarios) -> Usuarios:
    usuario = session.exec(select(Usuarios).where(Usuarios.email == user.email)).first()

    if not usuario:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    raise HTTPException(status_code=400, detail='Usuário já cadastrado')

@router.put("/{id}")
def update_usuario(id: int, usuario: Usuarios, session: SessionDep):
    usuarioUpdate = session.get(Usuarios, id)

    if usuarioUpdate:
        usuarioUpdate.sqlmodel_update(usuario.model_dump(exclude_unset=True))
        session.add(usuarioUpdate)
        session.commit()
        session.refresh(usuarioUpdate)
        return usuarioUpdate
    
    raise HTTPException(status_code=400, detail="O usuário não existe")

@router.delete('/{id}')
def deletar_usuarios(session: SessionDep, id: int) -> str:
    usuario = session.get(Usuarios, id)
    if usuario:
        session.delete(usuario)
        session.commit()
        return "Usuário deletado com sucesso"

    raise HTTPException(status_code=400, detail="Usuário não existe")