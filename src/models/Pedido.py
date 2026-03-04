from pydantic import BaseModel
from models.DetallePedido import DetallePedido


class Pedido(BaseModel):
    id: int
    cliente_id: int
    fecha: str
    total: float
    estado: str
    metodo_pago: str
    productos: list[DetallePedido]
