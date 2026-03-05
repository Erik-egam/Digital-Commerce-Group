from typing import Iterable
from models.orm.cliente import Cliente as ClienteORM

def map_cliente(c: ClienteORM) -> dict:
    return {
        "id_cliente": c.id_cliente,
        "nombre": c.nombre,
        "telefono": c.telefono,
        "direccion": c.direccion,
    }

def map_clientes(items: Iterable[ClienteORM]) -> list[dict]:
    return [map_cliente(x) for x in items]
