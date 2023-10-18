from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.login.router_login import router as router_login
from routers.menu.router_menu import router as router_menu
from routers.produto.router_produto import router as router_produto
from routers.estoque.router_estoque import router as router_estoque
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="./src/public/static"), name="static")

app.include_router(router_login, prefix="/login")
app.include_router(router_menu, prefix="/menu")
app.include_router(router_produto, prefix="/produto")
app.include_router(router_estoque, prefix="/estoque")

if __name__ == "__main__":
    uvicorn.run(app="app:app", host="localhost", port=8000, reload=True)