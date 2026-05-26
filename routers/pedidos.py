from fastapi import Depends, APIRouter, HTTPException
from database.database import get_session
from typing import Annotated
from sqlmodel import select, Session
from models.models import Pedido, Usuario

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get('/')
def listar_pedidos(session: SessionDep) -> list[Pedido]:
    pedidos = session.exec(select(Pedido)).all()
    return pedidos

@router.get('/{id}')
def listar_pedidos_id(session: SessionDep, id: int) -> Pedido:
    pedido = session.get(Pedido, id)
    if pedido:
        return pedido
    
    raise HTTPException(status_code=400, detail='O pedido não existe')

@router.post('/')
def cadastrar_pedidos(session: SessionDep, pedido: Pedido) -> Pedido:
    verificarID = session.get(Usuario, pedido.usuario_id)
    
    if verificarID:
        session.add(pedido)
        session.commit()
        session.refresh(pedido)
        return pedido
    
    raise HTTPException(status_code=400, detail='O usuário não existe')

@router.put('/{id}')
def editar_pedidos(session: SessionDep, pedido: Pedido, id: int) -> Pedido:
    pedidoUpdate = session.get(Pedido, id)
    verificarId = session.get(Usuario, pedido.usuario_id)
    if pedidoUpdate:
        if verificarId:
            pedidoUpdate.sqlmodel_update(pedido.model_dump(exclude_unset=True))
            session.add(pedidoUpdate)
            session.commit()
            session.refresh(pedidoUpdate)
            return pedidoUpdate
        raise HTTPException(status_code=400, detail="O usuário não existe")
    
    raise HTTPException(status_code=400, detail='Pedido não encontrado')

@router.delete('/{id}')
def excluir_pedidos(session: SessionDep, id: int):
    pedido = session.get(Pedido, id)
    if pedido:
        session.delete(pedido)
        session.commit()
        return "Pedido deletado com sucesso"
    
    raise HTTPException(status_code=400, detail="O pedido não existe")