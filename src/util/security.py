

from typing import Optional
from fastapi import Request
from src.repository.UsuarioRepo import UsuarioRepo

from src.sql.models.UsuarioModel import Usuario


async def obter_usuario_logado(request: Request) -> Optional[Usuario]:
    try:
        token = request.cookies["auth_token"]
        if token.strip() == "":
            return None
        usuario = UsuarioRepo.ObterUsuarioPorToken(token)
        return usuario
    
    except KeyError:
        return None