from pydantic import BaseModel

class DetallePedido(BaseModel):
    id: int
    pedido_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float
    total: float