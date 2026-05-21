from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from datetime import datetime

class Produto(SQLModel, table=True):
    __tablename__ = "usuarios"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)
    email: str = Field(max_length=150, unique=True)
    senha_hash: str = Field(max_length=255)

    pedidos: list["Produto"] = Relationship(back_populates="usuario")
    enderecos: list["Estoque"] = Relationship(back_populates="usuario")
    avaliacoes: list["Avaliacao"] = Relationship(back_populates="usuario")

class Papel(SQLModel, table=True):
    __tablename__ = "papeis"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=50, unique=True)

class UsuarioPapel(SQLModel, table=True):
    __tablename__ = "usuario_papeis"
    usuario_id: int = Field(primary_key=True, foreign_key="usuarios.id")
    papel_id: int = Field(primary_key=True, foreign_key="papeis.id")

class Produto(SQLModel, table=True):
    __tablename__ = "produtos"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=150)
    descricao: str
    preco: int

    avaliacoes: list["Avaliacao"] = Relationship(back_populates="produto")
    estoque: list["Estoque"] = Relationship(back_populates="produto")

class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)

class ProdutoCategoria(SQLModel, table=True):
    __tablename__ = "produtos_categoria"
    produto_id: int = Field(primary_key=True, foreign_key="produtos.id")
    categoria_id: int = Field(primary_key=True, foreign_key="categorias.id")

class Produto(SQLModel, table=True):
    __tablename__ = "pedidos"
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    total: int
    status: str = Field(max_length=50)
    
    usuario: "Produto" = Relationship(back_populates='pedidos')
    pagamentos: list["Avaliacao"] = Relationship(back_populates="pedido")

class ItemPedido(SQLModel, table=True):
    __tablename__ = "itens_pedidos"
    pedido_id: int = Field(primary_key=True, foreign_key="pedidos.id")
    produto_id: int = Field(primary_key=True, foreign_key="produtos.id")
    quantidade: int
    preco: int
    
class Avaliacao(SQLModel, table=True):
    __tablename__ = "pagamentos"
    id: int | None = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedidos.id")
    valor: Decimal = Field(max_digits=10, decimal_places=2)
    metodo: str = Field(max_length=50)
    status: str = Field(max_length=50)

    pedido: "Produto" = Relationship(back_populates="pagamentos")

class Estoque(SQLModel, table=True):
    __tablename__ = "enderecos"
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    rua: str = Field(max_length=150)
    cidade: str = Field(max_length=100)
    estado: str = Field(max_length=100)
    cep: str = Field(max_length=20)

    usuario: "Produto" = Relationship(back_populates='enderecos')

class Avaliacao(SQLModel, table=True):
    __tablename__ = "avaliacoes"
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    produto_id: int = Field(foreign_key="produtos.id")
    nota: int
    comentario: str

    usuario: "Produto" = Relationship(back_populates='avaliacoes')
    produto: "Produto" = Relationship(back_populates='avaliacoes')

class Estoque(SQLModel, table=True):
    __tablename__ = "estoque"
    id: int | None = Field(default=None, primary_key=True)
    produto_id: int = Field(foreign_key="produtos.id")
    quantidade: int

    produto: "Produto" = Relationship(back_populates='estoque')