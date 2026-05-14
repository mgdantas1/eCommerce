from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal

class Usuarios(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)
    email: str = Field(max_length=150, unique=True)
    senha_hash: str = Field(max_length=255)

    pedidos: list["Pedidos"] = Relationship(back_populates="usuario")
    enderecos: list["Enderecos"] = Relationship(back_populates="usuario")
    avaliacoes: list["Avaliacoes"] = Relationship(back_populates="usuario")

class Papeis(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=50, unique=True)

class Produtos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=150)
    descricao: str
    preco: int

    avaliacoes: list["Avaliacoes"] = Relationship(back_populates="produto")
    estoque: list["Estoque"] = Relationship(back_populates="produto")

class Categorias(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100)

class Pedidos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    total: int
    status: str = Field(max_length=50)
    
    usuario: "Usuarios" = Relationship(back_populates='pedidos')
    pagamentos: list["Pagamentos"] = Relationship(back_populates="pedido")

class Pagamentos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedidos.id")
    valor: Decimal = Field(max_digits=10, decimal_places=2)
    metodo: str = Field(max_length=50)

    pedido: "Pedidos" = Relationship(back_populates="pagamentos")

class Enderecos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    rua: str = Field(max_length=150)
    cidade: str = Field(max_length=100)
    estado: str = Field(max_length=100)
    cep: str = Field(max_length=20)

    usuario: "Usuarios" = Relationship(back_populates='enderecos')

class Avaliacoes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    produto_id: int = Field(foreign_key="produtos.id")
    nota: int
    comentario: str

    usuario: "Usuarios" = Relationship(back_populates='avaliacoes')
    produto: "Produtos" = Relationship(back_populates='avaliacoes')

class Estoque(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    produto_id: int = Field(foreign_key="produtos.id")
    quantidade: int

    produto: "Produtos" = Relationship(back_populates='estoque')