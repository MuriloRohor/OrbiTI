from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from src.routers.login.router_login import router as router_login
from src.routers.menu.router_menu import router as router_menu
from src.routers.produto.router_produto import router as router_produto
from src.routers.estoque.router_estoque import router as router_estoque
from src.routers.relatorio.router_relatorio import router as router_relatorio
from src.routers.solicitacao.router_solicitacao import router as router_solicitacao
from src.routers.fornecedor.router_fornecedor import router as router_fornecedor
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.mount("/static", StaticFiles(directory="src/public/static"), name="static")


app.include_router(router_login, prefix="/login")
app.include_router(router_menu, prefix="/menu")
app.include_router(router_produto, prefix="/produto")
app.include_router(router_estoque, prefix="/estoque")
app.include_router(router_relatorio, prefix="/relatorio")
app.include_router(router_solicitacao, prefix="/solicitacao")
app.include_router(router_fornecedor, prefix="/fornecedor")