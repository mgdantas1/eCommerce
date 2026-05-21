from fastapi import Depends, APIRouter, HTTPException
from database import get_session
from typing import Annotated
from sqlmodel import select, Session
from models import Produto, Produto

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get('/')
def listar_pedidos(session: SessionDep) -> list[Produto]:
    pedidos = session.exec(select(Produto)).all()
    return pedidos

@router.post('/')
def cadastrar_pedidos(session: SessionDep, pedido: Produto) -> Produto:
    verificarID = session.get(Produto, pedido.usuario_id)
    
    if verificarID:
        session.add(pedido)
        session.commit()
        session.refresh(pedido)
        return pedido
    
    raise HTTPException(status_code=400, detail='Usuário não existe')

@router.put('/{id}')
def editar_pedidos(session: SessionDep, pedido: Produto, id: int) -> Produto:
    pedidoUpdate = session.get(Produto, id)
    verificarId = session.get(Produto, pedido.usuario_id)
    if pedidoUpdate:
        if verificarId:
            pedidoUpdate.model_copy(update=pedido.model_dump())
            session.add(pedidoUpdate)
            session.commit()
            session.refresh(pedidoUpdate)
            return pedidoUpdate
        raise HTTPException(status_code=400, detail="O usuário não existe")
    
    raise HTTPException(status_code=400, detail='Pedido não encontrado')

@router.delete('/{id}')
def excluir_pedidos(session: SessionDep, id: int):
    pedido = session.get(Produto, id)
    if pedido:
        session.delete(pedido)
        session.commit()
        return "Pedido deletado com sucesso"
    
    raise HTTPException(status_code=400, detail="O pedido não existe")