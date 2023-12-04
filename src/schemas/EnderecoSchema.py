from pydantic import BaseModel

class EnderecoSchema(BaseModel):
    cep: int
    cidade: int
    logradouro: str
    bairro: str
    numero: int

    class Config:
        orm_mode = True


class EnderecoTest(BaseModel):
    cep: int
    cidade: int

    class Config:
        orm_mode = True