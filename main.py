from typing import Annotated
from sqlmodel import select, Session
from fastapi import FastAPI, Depends
from database import create_db, get_session
from contextlib import asynccontextmanager
from routers import users

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(users.router)

# # =-= PAPEIS =-=

# @app.get('/papeis')
# def listar_papeis(session: SessionDep) -> list[Papel]:
#     papeis = session.exec(select(Papel)).all()
#     return papeis

# @app.post('/papeis')
# def cadastrar_papeis(session: SessionDep, papel: Papel) -> Papel:
#     papelVerificar = session.exec(select(Papel).where(papel.nome == Papel.nome)).first()
#     if not papelVerificar:
#         session.add(papel)
#         session.commit()
#         session.refresh(papel)
#         return papel
    
#     raise HTTPException(status_code=400, detail="O papel já existe")
    
# @app.put('/papeis')
# def editar_papeis(session: SessionDep, id: int, papel: Papel) -> Papel:
#     papelUpdate = session.get(Papel, id)
#     if papelUpdate:
#         papelUpdate.nome = papel.nome
#         session.add(papelUpdate)
#         session.commit()
#         session.refresh(papelUpdate)
#         return papelUpdate
    
#     raise HTTPException(status_code=400, detail="O papel não existe")

# @app.delete('/papeis')
# def excluir_papeis(session: SessionDep, id: int) -> str:
#     papel = session.get(Papel, id)
#     if papel:
#         session.delete(papel)
#         session.commit()
#         return "Papel deletado com sucesso"
    
#     raise HTTPException(status_code=400, detail="Papel não existe")

# # =-= PRODUTOS =-=

# @app.get('/produtos')
# def listar_produtos(session: SessionDep) -> list[Produto]:
#     produtos = session.exec(select(Produto)).all()
#     return produtos

# @app.post('/produtos')
# def adicionar_produtos(session: SessionDep, produto: Produto) -> Produto:
#     session.add(produto)
#     session.commit()
#     session.refresh(produto)
#     return produto

# @app.put('/produtos')
# def editar_produtos(session: SessionDep, produto: Produto, id: int) -> Produto:
#     produtoUpdate = session.get(Produto, id)
#     if produtoUpdate:
#         produtoUpdate.nome = produto.nome
#         produtoUpdate.descricao = produto.descricao
#         produtoUpdate.preco = produto.preco
#         session.add(produtoUpdate)
#         session.commit()
#         session.refresh(produtoUpdate)
#         return produtoUpdate

#     raise HTTPException(status_code=400, detail="O produto não existe")

# @app.delete('/produtos')
# def excluir_produtos(session: SessionDep, id: int) -> str:
#     produto = session.get(Produto, id)
#     if produto:
#         session.delete(produto)
#         session.commit()
#         return "Produto deletado com sucesso"
    
#     raise HTTPException(status_code=400, detail='O produto não existe')

# # =-= CATEGORIAS =-=

# @app.get('/categorias')
# def listar_categoria(session: SessionDep) -> list[Categoria]:
#     categorias = session.exec(select(Categoria)).all()
#     return categorias

# @app.post('/categorias')
# def cadastrar_categoria(session: SessionDep, categoria: Categoria) -> Categoria:
#     session.add(categoria)
#     session.commit()
#     session.refresh(categoria)
#     return categoria

# @app.put('/categorias')
# def editar_categoria(session: SessionDep, categoria: Categoria, id: int) -> Categoria:
#     categoriaUpdate = session.get(Categoria, id)
#     if categoriaUpdate:
#         categoriaUpdate.nome = categoria.nome
#         session.add(categoriaUpdate)
#         session.commit()
#         session.refresh(categoriaUpdate)
#         return categoriaUpdate
    
#     raise HTTPException(status_code=400, detail='Categoria não encontrada')

# @app.delete('/categorias')
# def excluir_categoria(session: SessionDep, id: int):
#     categoria = session.get(Categoria, id)
#     if categoria:
#         session.delete(categoria)
#         session.commit()
#         return 'Categoria deletada com sucesso'
    
#     raise HTTPException(status_code=400, detail="Categoria não encontrada")

# # =-= PEDIDOS =-=

# @app.get('/pedidos')
# def listar_pedidos(session: SessionDep) -> list[Pedido]:
#     pedidos = session.exec(select(Pedido)).all()
#     return pedidos

# @app.post('/pedidos')
# def cadastrar_pedidos(session: SessionDep, pedido: Pedido) -> Pedido:
#     verificarID = session.get(Usuario, pedido.usuario_id)
#     if verificarID:
#         session.add(pedido)
#         session.commit()
#         session.refresh(pedido)
#         return pedido
    
#     raise HTTPException(status_code=400, detail='Usuário não existe')

# @app.put('/pedidos')
# def editar_pedidos(session: SessionDep, pedido: Pedido, id: int) -> Pedido:
#     pedidoUpdate = session.get(Pedido, id)
#     if pedidoUpdate:
#         pedidoUpdate.total = pedido.total
#         pedidoUpdate.status = pedido.status
#         session.add(pedidoUpdate)
#         session.commit()
#         session.refresh(pedidoUpdate)
#         return pedidoUpdate
    
#     raise HTTPException(status_code=400, detail='Pedido não encontrado')

# @app.delete('/pedidos')
# def excluir_pedidos(session: SessionDep, id: int):
#     pedido = session.get(Pedido, id)
#     if pedido:
#         session.delete(pedido)
#         session.commit()
#         return "Pedido deletado com sucesso"
    
#     raise HTTPException(status_code=400, detail="O pedido não existe")

# # =-= ENDEREÇOS =-=

# @app.get('/enderecos')
# def listar_enderecos(session: SessionDep) -> list[Endereco]:
#     enderecos = session.exec(select(Endereco)).all()
#     return enderecos

# @app.post('/enderecos')
# def cadastrar_enderecos(session: SessionDep, endereco: Endereco) -> Endereco:
#     session.add(endereco)
#     session.commit()
#     session.refresh(endereco)
#     return endereco

