from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import web_routes
import uvicorn

app = FastAPI()

# Montando arquivos estáticos
app.mount("/static", StaticFiles(directory="../public/static"), name="static")

# Incluindo rotas de renderização
app.include_router(web_routes.router)

if __name__ == "__main__":
    uvicorn.run(app="app:app", host="localhost", port=8000, reload=True)