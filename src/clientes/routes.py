from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.sql_alquemy_conexion import get_db
from models.mappers.Cliente import map_clientes, map_cliente
from .service import listar, obtener, crear, actualizar, eliminar

router = APIRouter()

class ClienteCreate(BaseModel):
    id_cliente: str
    nombre: str
    telefono: str | None = None
    direccion: str | None = None

class ClienteUpdate(BaseModel):
    nombre: str
    telefono: str | None = None
    direccion: str | None = None

@router.get("/", tags=["clientes"])
def listar_clientes(db: Session = Depends(get_db)):
    return map_clientes(listar(db))

@router.get("/{id_cliente}", tags=["clientes"])
def obtener_cliente(id_cliente: str, db: Session = Depends(get_db)):
    c = obtener(db, id_cliente)
    if not c:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return map_cliente(c)

@router.post("/", tags=["clientes"])
def crear_cliente(payload: ClienteCreate, db: Session = Depends(get_db)):
    try:
        c = crear(db, payload.id_cliente, payload.nombre, payload.telefono, payload.direccion)
        return map_cliente(c)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{id_cliente}", tags=["clientes"])
def actualizar_cliente(id_cliente: str, payload: ClienteUpdate, db: Session = Depends(get_db)):
    try:
        c = actualizar(db, id_cliente, payload.nombre, payload.telefono, payload.direccion)
        return map_cliente(c)
    except ValueError as e:
        raise HTTPException(status_code=404 if "no encontrado" in str(e).lower() else 400, detail=str(e))

@router.delete("/{id_cliente}", tags=["clientes"])
def eliminar_cliente(id_cliente: str, db: Session = Depends(get_db)):
    try:
        eliminar(db, id_cliente)
        return {"ok": True}
    except ValueError as e:
        raise HTTPException(status_code=404 if "no encontrado" in str(e).lower() else 400, detail=str(e))
