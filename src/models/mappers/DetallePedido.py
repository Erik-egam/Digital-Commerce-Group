from typing import Iterable
from models.orm.detalle_pedido import DetallePedido as DetalleORM

def to_float(x):
    return float(x) if x is not None else None

def map_detalle(d: DetalleORM) -> dict:
    return {
        "id_detalle": d.id_detalle,
        "id_pedido": d.id_pedido,
        "id_producto": d.id_producto,
        "cantidad": d.cantidad,
        "subtotal": to_float(d.subtotal),
    }

def map_detalles(items: Iterable[DetalleORM]) -> list[dict]:
    return [map_detalle(x) for x in items]
