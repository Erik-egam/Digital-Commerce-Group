from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.sql_alquemy_conexion import get_db
from models.mappers.Producto import map_productos, map_producto
from .service import listar, obtener, crear, actualizar, eliminar

router = APIRouter()

# Modelos de validación (Pydantic)
class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int

class ProductoUpdate(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float
    stock: int

@router.get("/", tags=["productos"])
def listar_productos(db: Session = Depends(get_db)):
    return map_productos(listar(db))

@router.get("/{id_producto}", tags=["productos"])
def obtener_producto(id_producto: int, db: Session = Depends(get_db)):
    p = obtener(db, id_producto)
    if not p:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return map_producto(p)

@router.post("/", tags=["productos"], status_code=201)
def crear_producto(payload: ProductoCreate, db: Session = Depends(get_db)):
    try:
        p = crear(db, payload.nombre, payload.descripcion, payload.precio, payload.stock)
        return map_producto(p)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{id_producto}", tags=["productos"])
def actualizar_producto(id_producto: int, payload: ProductoUpdate, db: Session = Depends(get_db)):
    try:
        p = actualizar(db, id_producto, payload.nombre, payload.descripcion, payload.precio, payload.stock)
        return map_producto(p)
    except ValueError as e:
        raise HTTPException(status_code=404 if "no encontrado" in str(e).lower() else 400, detail=str(e))

@router.delete("/{id_producto}", tags=["productos"])
def eliminar_producto(id_producto: int, db: Session = Depends(get_db)):
    try:
        eliminar(db, id_producto)
        return {"ok": True}
    except ValueError as e:
        raise HTTPException(status_code=404 if "no encontrado" in str(e).lower() else 400, detail=str(e))