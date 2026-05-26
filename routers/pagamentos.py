# from fastapi import Depends, HTTPException, APIRouter
# from sqlmodel import select, Session
# from typing import Annotated
# from models import Avaliacao, Produto
# from database.database import get_session

# SessionDep = Annotated[Session, Depends(get_session)]

# router = APIRouter(prefix="/pagamentos", tags=["pagamentos"])

# @router.get("/")
# def listar_pagamentos(session: SessionDep) -> list[Avaliacao]:
#     pagamentos = session.exec(select(Avaliacao)).all()
#     return pagamentos

# @router.post("/")
# def cadastrar_pagamentos(session: SessionDep, pagamento: Avaliacao) -> Avaliacao:
#     verificarId = session.get(Produto, pagamento.pedido_id)
#     if verificarId:
#         session.add(pagamento)
#         session.commit()
#         session.refresh(pagamento)
#         return pagamento
    
#     raise HTTPException(status_code=400, detail="Usuário não existe")

# @router.put("/{id}")
# def editar_pagamentos(session: SessionDep, id: int, pagamento: Avaliacao) -> Avaliacao:
#     pagamentoUpdate = session.get(Avaliacao, id)
#     verificarId = session.get(Produto, pagamento.pedido_id)

#     if pagamentoUpdate:
#         if verificarId:
#             pagamentoUpdate.sqlmodel_update(pagamento.model_dump(exclude_unset=True))
#             pagamento.add(pagamentoUpdate)
#             pagamento.commit()
#             pagamento.refresh(pagamentoUpdate)
#             return pagamentoUpdate
        
#         raise HTTPException(status_code=400, detail="O usuário não existe")
    
#     raise HTTPException(status_code=400, detail="O pagamento não existe")

# @router.delete("/{id}")
# def excluir_pagamentos(session: SessionDep, id: int):
#     pagamento = session.get(Avaliacao, id)  

#     if pagamento:
#         session.delete(pagamento)
#         session.commit()
#         return "O pagamento foi excluído com sucesso"

#     raise HTTPException(status_code=400, detail="O pagamento não existe")