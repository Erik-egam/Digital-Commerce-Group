from typing import Iterable
from models.orm.producto import Producto as ProductoORM

def to_float(x):
    return float(x) if x is not None else None

def map_producto(p: ProductoORM) -> dict:
    return {
        "id_producto": p.id_producto,
        "nombre": p.nombre,
        "descripcion": p.descripcion,
        "precio": to_float(p.precio),
        "stock": p.stock,
    }

def map_productos(items: Iterable[ProductoORM]) -> list[dict]:
    return [map_producto(x) for x in items]
