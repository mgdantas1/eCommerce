# from fastapi import Depends, HTTPException, APIRouter
# from database.database import get_session
# from sqlmodel import Session, select
# from typing import Annotated
# from models import Categoria

# SessionDep = Annotated[Session, Depends(get_session)]

# router = APIRouter(prefix="/categorias", tags=["categorias"])

# @router.get('/')
# def listar_categoria(session: SessionDep) -> list[Categoria]:
#     categorias = session.exec(select(Categoria)).all()
#     return categorias

# @router.post('/')
# def cadastrar_categoria(session: SessionDep, categoria: Categoria) -> Categoria:
#     session.add(categoria)
#     session.commit()
#     session.refresh(categoria)
#     return categoria

# @router.put('/{id}')
# def editar_categoria(session: SessionDep, categoria: Categoria, id: int) -> Categoria:
#     categoriaUpdate = session.get(Categoria, id)
#     if categoriaUpdate:
#         categoriaUpdate.sqlmodel_update(categoria.model_dump(exclude_unset=True))
#         session.add(categoriaUpdate)
#         session.commit()
#         session.refresh(categoriaUpdate)
#         return categoriaUpdate
    
#     raise HTTPException(status_code=400, detail='Categoria não encontrada')

# @router.delete('/{id}')
# def excluir_categoria(session: SessionDep, id: int):
#     categoria = session.get(Categoria, id)
#     if categoria:
#         session.delete(categoria)
#         session.commit()
#         return 'Categoria deletada com sucesso'
    
#     raise HTTPException(status_code=400, detail="Categoria não encontrada")