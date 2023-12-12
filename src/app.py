import uvicorn
from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from src.routers.login.router_login import router as router_login
from src.routers.menu.router_menu import router as router_menu
from src.routers.produto.router_produto import router as router_produto
from src.routers.estoque.router_estoque import router as router_estoque
from src.routers.relatorio.router_relatorio import router as router_relatorio
from src.routers.solicitacao.router_solicitacao import router as router_solicitacao
from src.routers.fornecedor.router_fornecedor import router as router_fornecedor
from src.routers.categoria.router_categoria import router as router_categoria
from src.util.init_user import init_user


from src.util.security import atualizar_cookie_autenticacao


init_user()


app = FastAPI()
app.middleware("http")(atualizar_cookie_autenticacao)

app.mount("/static", StaticFiles(directory="src/public/static"), name="static")


app.include_router(router_login)
app.include_router(router_menu, prefix="/menu")
app.include_router(router_produto, prefix="/produto")
app.include_router(router_estoque, prefix="/estoque")
app.include_router(router_relatorio, prefix="/relatorio")
app.include_router(router_solicitacao, prefix="/solicitacao")
app.include_router(router_fornecedor, prefix="/fornecedor")
app.include_router(router_categoria, prefix="/categoria")