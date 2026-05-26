from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import select, Session
from typing import Annotated
from models.models import Estoque, Produto
from database.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/estoque", tags=["estoque"])

@router.get('/')
def listar_estoque(session: SessionDep) -> list[Estoque]:
    estoque = session.exec(select(Estoque)).all()
    return estoque

@router.get('/{id}')
def listar_estoque_id(session: SessionDep, id: int) -> Estoque:
    estoque = session.get(Estoque, id)
    if estoque:
        return estoque
    
    raise HTTPException(status_code=400, detail="O estoque não existe")

@router.post('/')
def cadastrar_estoque(session: SessionDep, estoque: Estoque) -> Estoque:
    verificarID = session.get(Produto, estoque.produto_id)
    if verificarID:
        session.add(estoque)
        session.commit()
        session.refresh(estoque)
        return estoque

    raise HTTPException(status_code=400, detail="O produto não existe")

@router.put("/{id}")
def editar_estoque(session: SessionDep, id: int, estoque: Estoque) -> Estoque:
    estoqueUpdate = session.get(Estoque, id)
    if estoqueUpdate:
        estoqueUpdate.sqlmodel_update(estoque.model_dump(exclude_unset=True))
        session.add(estoqueUpdate)
        session.commit()
        session.refresh(estoqueUpdate)
        return estoqueUpdate
    
    raise HTTPException(status_code=400, detail="O estoque não existe")

@router.delete("/{id}")
def excluir_estoque(session: SessionDep, id: int):
    estoque = session.get(Estoque, id)
    if estoque:
        session.delete(estoque)
        session.commit()
        return "Estoque excluído com sucesso"

    raise HTTPException(status_code=400, detail="O estoque não existe") 