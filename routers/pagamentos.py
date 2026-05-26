from fastapi import Depends, HTTPException, APIRouter
from sqlmodel import select, Session
from typing import Annotated
from models.models import Pagamento, Pedido
from database.database import get_session

SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])

@router.get("/")
def listar_pagamentos(session: SessionDep) -> list[Pagamento]:
    pagamentos = session.exec(select(Pagamento)).all()
    return pagamentos

@router.get("/{id}")
def listar_pagamento_id(session: SessionDep, id: int) -> Pagamento:
    pagamento = session.get(Pagamento, id)
    if pagamento:
        return pagamento
    
    raise HTTPException(status_code=400, detail="O pagamento não existe")

@router.post("/")
def cadastrar_pagamentos(session: SessionDep, pagamento: Pagamento) -> Pagamento:
    verificarId = session.get(Pedido, pagamento.pedido_id)
    if verificarId:
        session.add(pagamento)
        session.commit()
        session.refresh(pagamento)
        return pagamento
    
    raise HTTPException(status_code=400, detail="O pedido não existe")

@router.put("/{id}")
def editar_pagamentos(session: SessionDep, id: int, pagamento: Pagamento) -> Pagamento:
    pagamentoUpdate = session.get(Pagamento, id)

    if pagamentoUpdate:
        verificarID = session.get(Pedido, pagamento.pedido_id)
        
        if verificarID:
            pagamentoUpdate.sqlmodel_update(pagamento.model_dump(exclude_unset=True))
            session.add(pagamentoUpdate)
            session.commit()
            session.refresh(pagamentoUpdate)
            return pagamentoUpdate
            
        raise HTTPException(status_code=400, detail="O pedido não existe")
    
    raise HTTPException(status_code=400, detail="O pagamento não existe")

@router.delete("/{id}")
def excluir_pagamentos(session: SessionDep, id: int):
    pagamento = session.get(Pagamento, id)  

    if pagamento:
        session.delete(pagamento)
        session.commit()
        return "O pagamento foi excluído com sucesso"

    raise HTTPException(status_code=400, detail="O pagamento não existe")