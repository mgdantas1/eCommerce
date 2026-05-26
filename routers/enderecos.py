# from fastapi import Depends, HTTPException, APIRouter
# from sqlmodel import select, Session
# from typing import Annotated
# from models import Estoque, Produto
# from database.database import get_session

# SessionDep = Annotated[Session, Depends(get_session)]

# router = APIRouter(prefix="/enderecos", tags=["enderecos"])

# @router.get('/')
# def listar_enderecos(session: SessionDep) -> list[Estoque]:
#     enderecos = session.exec(select(Estoque)).all()
#     return enderecos

# @router.post('/')
# def cadastrar_enderecos(session: SessionDep, endereco: Estoque) -> Estoque:
#     verificarID = session.get(Produto, endereco.usuario_id)
#     if verificarID:
#         session.add(endereco)
#         session.commit()
#         session.refresh(endereco)
#         return endereco

#     raise HTTPException(status_code=400, detail="O usuário não existe")

# @router.put("/{id}")
# def editar_enderecos(session: SessionDep, id: int, endereco: Estoque) -> Estoque:
#     enderecoUpdate = session.get(Estoque, id)
#     verificarId = session.get(Produto, endereco.usuario_id)
#     if enderecoUpdate:
#         if verificarId:
#             enderecoUpdate.sqlmodel_update(endereco.model_dump(exclude_unset=True))
#             session.add(enderecoUpdate)
#             session.commit()
#             session.refresh(enderecoUpdate)
#             return enderecoUpdate
#         raise HTTPException(status_code=400, detail="O usuário não existe")
    
#     raise HTTPException(status_code=400, detail="O endereço não existe")

# @router.delete("/{id}")
# def excluir_enderecos(session: SessionDep, id: int):
#     endereco = session.get(Estoque, id)
#     if endereco:
#         session.delete(endereco)
#         session.commit()
#         return "Endereço excluído com sucesso"

#     raise HTTPException(status_code=400, detail="O usuário do endereço não existe") 