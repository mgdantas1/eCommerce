# from fastapi import Depends, HTTPException, APIRouter
# from sqlmodel import select, Session
# from typing import Annotated
# from models import Avaliacao, Produto, Produto
# from database.database import get_session

# SessionDep = Annotated[Session, Depends(get_session)]

# router = APIRouter(prefix="/avaliacoes", tags=["avaliacoes"])

# @router.get("/")
# def listar_avaliacoes(session: SessionDep) -> list[Avaliacao]:
#     avaliacoes = session.exec(select(Avaliacao)).all()
#     return avaliacoes

# @router.post("/")
# def cadastrar_avaliacoes(session: SessionDep, avaliacao: Avaliacao) -> Avaliacao:
#     verificarIdUser = session.get(Produto, avaliacao.usuario_id)
#     verificarIdProduto = session.get(Produto, avaliacao.produto_id)
#     if verificarIdUser:
#         if verificarIdProduto:
#             session.add(avaliacao)
#             session.commit()
#             session.refresh(avaliacao)
#             return avaliacao
#         raise HTTPException(status_code=400, detail="O produto nã existe")
    
#     raise HTTPException(status_code=400, detail="Usuário não existe")

# @router.put("/{id}")
# def editar_avaliacoes(session: SessionDep, id: int, avaliacao: Avaliacao) -> Avaliacao:
#     avaliacaoUpdate = session.get(Avaliacao, id)
#     verificarIdUser = session.get(Produto, avaliacao.usuario_id)
#     verificarIdProduto = session.get(Produto, avaliacao.produto_id)

#     if avaliacaoUpdate:
#         if verificarIdUser:
#             if verificarIdProduto:
#                 avaliacaoUpdate.sqlmodel_update(avaliacao.model_dump(exclude_unset=True))
#                 avaliacao.add(avaliacaoUpdate)
#                 avaliacao.commit()
#                 avaliacao.refresh(avaliacaoUpdate)
#                 return avaliacaoUpdate
#             raise HTTPException(status_code=400, detail="O produto não existe")
        
#         raise HTTPException(status_code=400, detail="O usuário não existe")
    
#     raise HTTPException(status_code=400, detail="O pagamento não existe")

# @router.delete("/{id}")
# def excluir_avaliacoes(session: SessionDep, id: int):
#     avaliacao = session.get(Avaliacao, id)  

#     if avaliacao:
#         session.delete(avaliacao)
#         session.commit()
#         return "O pagamento foi excluído com sucesso"

#     raise HTTPException(status_code=400, detail="O pagamento não existe")