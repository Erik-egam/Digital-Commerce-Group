from typing import Iterable
from models.orm.pedido import Pedido as PedidoORM
from .DetallePedido import map_detalles

def to_float(x):
    return float(x) if x is not None else None

def to_iso(dt):
    return dt.isoformat() if dt is not None else None

def map_pedido(p: PedidoORM) -> dict:
    return {
        "id_pedido": p.id_pedido,
        "id_cliente": p.id_cliente,
        "fecha": to_iso(p.fecha),
        "total": to_float(p.total),
        "estado": p.estado,
        "metodo_pago": p.metodo_pago,
        "detalles": map_detalles(p.detalles) if hasattr(p, "detalles") and p.detalles is not None else [],
    }

def map_pedidos(items: Iterable[PedidoORM]) -> list[dict]:
    return [map_pedido(x) for x in items]
