from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nombre: str
    telefono: str
    direccion: str
