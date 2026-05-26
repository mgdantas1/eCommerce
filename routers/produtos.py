# from fastapi import Depends, APIRouter, HTTPException
# from typing import Annotated
# from sqlmodel import Session, select
# from models import Produto
# from database.database import get_session

# SessionDep = Annotated[Session, Depends(get_session)]

# router = APIRouter(prefix="/produtos", tags=["produtos"])

# @router.get('/')
# def listar_produtos(session: SessionDep) -> list[Produto]:
#     produtos = session.exec(select(Produto)).all()
#     return produtos

# @router.post('/')
# def cadastrar_produtos(session: SessionDep, produto: Produto) -> Produto:
#     session.add(produto)
#     session.commit()
#     session.refresh(produto)
#     return produto

# @router.put('/{id}')
# def editar_produtos(session: SessionDep, produto: Produto, id: int) -> Produto:
#     produtoUpdate = session.get(Produto, id)
#     if produtoUpdate:
#         produtoUpdate.sqlmodel_update(produto.model_dump(exclude_unset=True))
#         session.add(produtoUpdate)
#         session.commit()
#         session.refresh(produtoUpdate)
#         return produtoUpdate

#     raise HTTPException(status_code=400, detail="O produto não existe")

# @router.delete('/{id}')
# def excluir_produtos(session: SessionDep, id: int) -> str:
#     produto = session.get(Produto, id)
#     if produto:
#         session.delete(produto)
#         session.commit()
#         return "Produto deletado com sucesso"
    
#     raise HTTPException(status_code=400, detail='O produto não existe')