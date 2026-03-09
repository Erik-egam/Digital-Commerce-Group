from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List

from config.sql_alquemy_conexion import get_db
from models.mappers.Pedido import map_pedidos, map_pedido
from pedidos.service import listar, obtener, crear, actualizar, eliminar

router = APIRouter()

class PedidoUpdate(BaseModel):
    estado: str

class DetallePedidoCreate(BaseModel):
    id_producto: int
    cantidad: int

class PedidoCreate(BaseModel):
    id_cliente: str
    estado: str
    metodo_pago: str
    detalles: List[DetallePedidoCreate]


@router.get("/", tags=["pedidos"])
def listar_pedidos(db: Session = Depends(get_db)):
    return map_pedidos(listar(db))


@router.get("/{id_pedido}", tags=["pedidos"])
def obtener_pedido(id_pedido: int, db: Session = Depends(get_db)):
    p = obtener(db, id_pedido)

    if not p:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    return map_pedido(p)


@router.post("/", tags=["pedidos"])
def crear_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    try:
        nuevo = crear(db, pedido)
        return map_pedido(nuevo)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{id_pedido}", tags=["pedidos"])
def actualizar_pedido(id_pedido: int, payload: PedidoUpdate, db: Session = Depends(get_db)):
    try:
        p = actualizar(db, id_pedido, payload.estado)
        return map_pedido(p)

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{id_pedido}", tags=["pedidos"])
def eliminar_pedido(id_pedido: int, db: Session = Depends(get_db)):
    try:
        eliminar(db, id_pedido)
        return {"ok": True}

    except ValueError as e:
        raise HTTPException(
            status_code=404 if "no encontrado" in str(e).lower() else 400,
            detail=str(e)
        )