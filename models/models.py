from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, UTC

class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100),
    email: EmailStr = Field(max_length=150, unique=True)
    senha_hash: str = Field(max_length=255)

    pedidos: list["Pedido"] = Relationship(back_populates="usuario")
    avaliacoes: list["Avaliacao"] = Relationship(back_populates="usuario")
    enderecos: list["Endereco"] = Relationship(back_populates="usuario")

class Papel(SQLModel, table=True):
    __tablename__ = "papeis"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=50, unique=True)

class UsuarioPapel(SQLModel, table=True):
    __tablename__ = "usuarios_papeis"
    usuario_id: int = Field(default=None,primary_key=True, foreign_key="usuarios.id")
    papel_id: int = Field(default=None,primary_key=True, foreign_key="papeis.id")


class Produto(SQLModel, table=True):
    __tablename__ = "produtos"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=150)
    preco: int 
    descricao: str 

    avaliacoes: list["Avaliacao"] = Relationship(back_populates="produto")
    estoque: list["Estoque"] = Relationship(back_populates="produto")

class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)

class ProdutoCategoria(SQLModel, table=True):
    __tablename__ = "produtos_categorias"
    produto_id: int = Field(default=None, primary_key=True,foreign_key="produtos.id")
    categoria_id: int = Field(default=None, primary_key=True,foreign_key="categorias.id")

class Pedido(SQLModel, table=True):
    __tablename__ = "pedidos"
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(default=None, foreign_key="usuarios.id")
    total: int
    status: str = Field(max_length=50)

    usuario: "Usuario" = Relationship(back_populates="pedidos")
    pagamentos: list["Pagamento"] = Relationship(back_populates="pedido")

class ItemPedido(SQLModel, table=True):
    __tablename__ = "itens_pedidos"
    pedido_id: int = Field(default=None,primary_key=True, foreign_key="pedidos.id")
    produto_id: int = Field(default=None, primary_key=True,foreign_key="produtos.id")
    quantidade: int = Field(default=None, nullable=False)
    preco: float = Field(default=None, nullable=False)

class Pagamento(SQLModel, table=True):
    __tablename__ = "pagamentos"
    id: int | None = Field(default=None, primary_key=True)
    pedido_id: int = Field(default=None, foreign_key="pedidos.id")
    valor: int
    metodo: str = Field(max_length=50)
    status: str = Field(max_length=50)

    pedido: "Pedido" = Relationship(back_populates="pagamentos")

class Endereco(SQLModel, table=True):
    __tablename__ = "enderecos"
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(default=None, foreign_key="usuarios.id")
    rua: str = Field(max_length=150)
    cidade: str = Field(max_length=100)
    estado: str = Field(max_length=100)
    cep: str = Field(max_length=20)

    usuario: "Usuario" = Relationship(back_populates="enderecos")

class Avaliacao(SQLModel, table=True):
    __tablename__ = "avaliacoes"
    id: int | None = Field(default=None, primary_key=True)
    produto_id: int = Field(default=None, foreign_key="produtos.id")
    usuario_id: int = Field(default=None, foreign_key="usuarios.id")
    nota: int 
    comentario: str 

    produto: "Produto" = Relationship(back_populates="avaliacoes")
    usuario: "Usuario" = Relationship(back_populates="avaliacoes")

class Estoque(SQLModel, table=True):
    __tablename__ = "estoque"
    id: int | None = Field(default=None, primary_key=True)
    produto_id: int = Field(default=None, foreign_key="produtos.id", unique=True)
    quantidade: int 

    produto: "Produto" = Relationship(back_populates="estoque")
