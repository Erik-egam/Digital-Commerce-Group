from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.sql_alquemy_conexion import get_db 
from productos.service import ProductoService
from models.mappers.Producto import map_productos, map_producto

router = APIRouter()

@router.get("/")
def listar_productos(db: Session = Depends(get_db)):
    servicio = ProductoService(db)
    productos = servicio.get_all()
    return map_productos(productos)

@router.get("/{id_producto}")
def obtener_producto(id_producto: int, db: Session = Depends(get_db)):
    servicio = ProductoService(db)
    producto = servicio.get_by_id(id_producto)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return map_producto(producto)

@router.post("/", status_code=201)
def crear_producto(datos: dict, db: Session = Depends(get_db)):
    servicio = ProductoService(db)
    nuevo = servicio.create(datos)
    return map_producto(nuevo)

@router.put("/{id_producto}")
def actualizar_producto(id_producto: int, datos: dict, db: Session = Depends(get_db)):
    servicio = ProductoService(db)
    actualizado = servicio.update(id_producto, datos)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return map_producto(actualizado)

@router.delete("/{id_producto}")
def eliminar_producto(id_producto: int, db: Session = Depends(get_db)):
    servicio = ProductoService(db)
    if not servicio.delete(id_producto):
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado exitosamente"}