from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.routerPage import router_page
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="./src/public/static"), name="static")

app.include_router(router_page)

if __name__ == "__main__":
    uvicorn.run(app="app:app", host="localhost", port=8000, reload=True)