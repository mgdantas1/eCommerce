from fastapi import FastAPI
from routers import papeis, usuarios, produtos, categorias, pedidos, pagamentos, avaliacoes, enderecos, estoque, auth

app = FastAPI()
app.include_router(usuarios.router)
app.include_router(papeis.router)
app.include_router(produtos.router)
app.include_router(categorias.router)
app.include_router(pedidos.router)
app.include_router(pagamentos.router)
app.include_router(enderecos.router)
app.include_router(avaliacoes.router)
app.include_router(estoque.router)
app.include_router(auth.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)