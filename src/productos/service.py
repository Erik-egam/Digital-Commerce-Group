from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.orm.producto import Producto

def listar(db: Session) -> list[Producto]:
    return db.query(Producto).all()

def obtener(db: Session, id_producto: int) -> Producto | None:
    return db.query(Producto).filter(Producto.id_producto == id_producto).first()

def crear(db: Session, nombre: str, descripcion: str | None, precio: float, stock: int) -> Producto:
    p = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
    db.add(p)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Error al crear el producto")
    db.refresh(p)
    return p

def actualizar(db: Session, id_producto: int, nombre: str, descripcion: str | None, precio: float, stock: int) -> Producto:
    p = obtener(db, id_producto)
    if not p:
        raise ValueError("Producto no encontrado")
    p.nombre = nombre
    p.descripcion = descripcion
    p.precio = precio
    p.stock = stock
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Error al actualizar el producto")
    db.refresh(p)
    return p

def eliminar(db: Session, id_producto: int):
    producto = db.get(Producto, id_producto)

    if not producto:
        raise ValueError("Producto no encontrado")

    try:
        db.delete(producto)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("No se puede eliminar el producto porque tiene relaciones")