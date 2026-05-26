from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import select, Session
from typing import Annotated
from models.models import Papel
from database.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/papeis", tags=['papeis'])

@router.get('/')
def listar_papeis(session: SessionDep) -> list[Papel]:
    papeis = session.exec(select(Papel)).all()
    return papeis

@router.get('/{id}')
def listar_papeis_id(session: SessionDep, id: int) -> Papel:
    papel = session.get(Papel, id)
    if papel:
        return papel
    
    raise HTTPException(status_code=400, detail="O papel não existe")

@router.post('/')
def cadastrar_papeis(session: SessionDep, papel: Papel) -> Papel:
    papelVerificar = session.exec(select(Papel).where(papel.nome == Papel.nome)).first()
    if not papelVerificar:
        session.add(papel)
        session.commit()
        session.refresh(papel)
        return papel
    
    raise HTTPException(status_code=400, detail="O papel já existe")
    
@router.put('/{id}')
def editar_papeis(session: SessionDep, id: int, papel: Papel) -> Papel:
    papelUpdate = session.get(Papel, id)
    if papelUpdate:
        papelUpdate.sqlmodel_update(papel.model_dump(exclude_unset=True))
        session.add(papelUpdate)
        session.commit()
        session.refresh(papelUpdate)
        return papelUpdate
    
    raise HTTPException(status_code=400, detail="O papel não existe")

@router.delete('/{id}')
def excluir_papeis(session: SessionDep, id: int) -> str:
    papel = session.get(Papel, id)
    if papel:
        session.delete(papel)
        session.commit()
        return "Papel deletado com sucesso"
    
    raise HTTPException(status_code=400, detail="Papel não existe")