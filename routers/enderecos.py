from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import select, Session
from typing import Annotated
from models.models import Endereco, Usuario
from database.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/enderecos", tags=["enderecos"])

@router.get('/')
def listar_enderecos(session: SessionDep) -> list[Endereco]:
    enderecos = session.exec(select(Endereco)).all()
    return enderecos

@router.get('/{id}')
def listar_endereco_id(session: SessionDep, id: int) -> Endereco:
    endereco = session.get(Endereco, id)

    if endereco:
        return endereco
    
    raise HTTPException(status_code=400, detail="O endereço não existe")

@router.post('/')
def cadastrar_enderecos(session: SessionDep, endereco: Endereco) -> Endereco:
    verificarID = session.get(Usuario, endereco.usuario_id)
    if verificarID:
        session.add(endereco)
        session.commit()
        session.refresh(endereco)
        return endereco

    raise HTTPException(status_code=400, detail="O usuário não existe")

@router.put("/{id}")
def editar_enderecos(session: SessionDep, id: int, endereco: Endereco) -> Endereco:
    enderecoUpdate = session.get(Endereco, id)
    verificarId = session.get(Usuario, endereco.usuario_id)
    if enderecoUpdate:
        if verificarId:
            enderecoUpdate.sqlmodel_update(endereco.model_dump(exclude_unset=True))
            session.add(enderecoUpdate)
            session.commit()
            session.refresh(enderecoUpdate)
            return enderecoUpdate
        raise HTTPException(status_code=400, detail="O usuário não existe")
    
    raise HTTPException(status_code=400, detail="O endereço não existe")

@router.delete("/{id}")
def excluir_enderecos(session: SessionDep, id: int):
    endereco = session.get(Endereco, id)
    if endereco:
        session.delete(endereco)
        session.commit()
        return "Endereço excluído com sucesso"

    raise HTTPException(status_code=400, detail="O usuário do endereço não existe") 