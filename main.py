from typing import Annotated
from sqlmodel import select, Session
from fastapi import FastAPI, Depends, HTTPException
from database import create_db, get_session
from contextlib import asynccontextmanager
from models import Usuarios, Papeis, Produtos, Categorias, Pedidos, Enderecos

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

# =-= USERS =-=

@app.get('/users')
def listar_usuarios(session: SessionDep) -> list[Usuarios]:
    usuarios = session.exec(select(Usuarios)).all()
    return usuarios

@app.post('/users')
def cadastrar_usuarios(session: SessionDep, user: Usuarios) -> Usuarios:
    usuario = session.exec(select(Usuarios).where(Usuarios.email == user.email)).first()
    if not usuario:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    raise HTTPException(status_code=400, detail='Usuário já cadastrado')

@app.put('/users')
def editar_usuarios(session: SessionDep, id: int, user: Usuarios) -> Usuarios:
    userUpdate = session.get(Usuarios, id)
    if userUpdate:
        userUpdate.nome = user.nome
        userUpdate.email = user.email
        userUpdate.senha_hash = user.senha_hash
        session.add(userUpdate)
        session.commit()
        session.refresh(userUpdate)
        return userUpdate
    
    raise HTTPException(status_code=400, detail="Usuário não existe")

@app.delete('/users')
def excluir_usuarios(session: SessionDep, id: int) -> str:
    usuario = session.get(Usuarios, id)
    if usuario:
        session.delete(usuario)
        session.commit()
        return "Usuário deletado com sucesso"

    raise HTTPException(status_code=400, detail="Usuário não existe")

# =-= PAPEIS =-=

@app.get('/papeis')
def listar_papeis(session: SessionDep) -> list[Papeis]:
    papeis = session.exec(select(Papeis)).all()
    return papeis

@app.post('/papeis')
def cadastrar_papeis(session: SessionDep, papel: Papeis) -> Papeis:
    papelVerificar = session.exec(select(Papeis).where(papel.nome == Papeis.nome)).first()
    if not papelVerificar:
        session.add(papel)
        session.commit()
        session.refresh(papel)
        return papel
    
    raise HTTPException(status_code=400, detail="O papel já existe")
    
@app.put('/papeis')
def editar_papeis(session: SessionDep, id: int, papel: Papeis) -> Papeis:
    papelUpdate = session.get(Papeis, id)
    if papelUpdate:
        papelUpdate.nome = papel.nome
        session.add(papelUpdate)
        session.commit()
        session.refresh(papelUpdate)
        return papelUpdate
    
    raise HTTPException(status_code=400, detail="O papel não existe")

@app.delete('/papeis')
def excluir_papeis(session: SessionDep, id: int) -> str:
    papel = session.get(Papeis, id)
    if papel:
        session.delete(papel)
        session.commit()
        return "Papel deletado com sucesso"
    
    raise HTTPException(status_code=400, detail="Papel não existe")

# =-= PRODUTOS =-=

@app.get('/produtos')
def listar_produtos(session: SessionDep) -> list[Produtos]:
    produtos = session.exec(select(Produtos)).all()
    return produtos

@app.post('/produtos')
def adicionar_produtos(session: SessionDep, produto: Produtos) -> Produtos:
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto

@app.put('/produtos')
def editar_produtos(session: SessionDep, produto: Produtos, id: int) -> Produtos:
    produtoUpdate = session.get(Produtos, id)
    if produtoUpdate:
        produtoUpdate.nome = produto.nome
        produtoUpdate.descricao = produto.descricao
        produtoUpdate.preco = produto.preco
        session.add(produtoUpdate)
        session.commit()
        session.refresh(produtoUpdate)
        return produtoUpdate

    raise HTTPException(status_code=400, detail="O produto não existe")

@app.delete('/produtos')
def excluir_produtos(session: SessionDep, id: int) -> str:
    produto = session.get(Produtos, id)
    if produto:
        session.delete(produto)
        session.commit()
        return "Produto deletado com sucesso"
    
    raise HTTPException(status_code=400, detail='O produto não existe')

# =-= CATEGORIAS =-=

@app.get('/categorias')
def listar_categoria(session: SessionDep) -> list[Categorias]:
    categorias = session.exec(select(Categorias)).all()
    return categorias

@app.post('/categorias')
def cadastrar_categoria(session: SessionDep, categoria: Categorias) -> Categorias:
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

@app.put('/categorias')
def editar_categoria(session: SessionDep, categoria: Categorias, id: int) -> Categorias:
    categoriaUpdate = session.get(Categorias, id)
    if categoriaUpdate:
        categoriaUpdate.nome = categoria.nome
        session.add(categoriaUpdate)
        session.commit()
        session.refresh(categoriaUpdate)
        return categoriaUpdate
    
    raise HTTPException(status_code=400, detail='Categoria não encontrada')

@app.delete('/categorias')
def excluir_categoria(session: SessionDep, id: int):
    categoria = session.get(Categorias, id)
    if categoria:
        session.delete(categoria)
        session.commit()
        return 'Categoria deletada com sucesso'
    
    raise HTTPException(status_code=400, detail="Categoria não encontrada")

# =-= PEDIDOS =-=

@app.get('/pedidos')
def listar_pedidos(session: SessionDep) -> list[Pedidos]:
    pedidos = session.exec(select(Pedidos)).all()
    return pedidos

@app.post('/pedidos')
def cadastrar_pedidos(session: SessionDep, pedido: Pedidos) -> Pedidos:
    verificarID = session.get(Usuarios, pedido.usuario_id)
    if verificarID:
        session.add(pedido)
        session.commit()
        session.refresh(pedido)
        return pedido
    
    raise HTTPException(status_code=400, detail='Usuário não existe')

@app.put('/pedidos')
def editar_pedidos(session: SessionDep, pedido: Pedidos, id: int) -> Pedidos:
    pedidoUpdate = session.get(Pedidos, id)
    if pedidoUpdate:
        pedidoUpdate.total = pedido.total
        pedidoUpdate.status = pedido.status
        session.add(pedidoUpdate)
        session.commit()
        session.refresh(pedidoUpdate)
        return pedidoUpdate
    
    raise HTTPException(status_code=400, detail='Pedido não encontrado')

@app.delete('/pedidos')
def excluir_pedidos(session: SessionDep, id: int):
    pedido = session.get(Pedidos, id)
    if pedido:
        session.delete(pedido)
        session.commit()
        return "Pedido deletado com sucesso"
    
    raise HTTPException(status_code=400, detail="O pedido não existe")

# =-= ENDEREÇOS =-=

@app.get('/enderecos')
def listar_enderecos(session: SessionDep) -> list[Enderecos]:
    enderecos = session.exec(select(Enderecos)).all()
    return enderecos

@app.post('/enderecos')
def cadastrar_enderecos(session: SessionDep, endereco: Enderecos) -> Enderecos:
    session.add(endereco)
    session.commit()
    session.refresh(endereco)
    return endereco

