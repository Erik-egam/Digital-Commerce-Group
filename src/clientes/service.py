from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.orm.cliente import Cliente

def listar(db: Session) -> list[Cliente]:
    return db.query(Cliente).all()

def obtener(db: Session, id_cliente: str) -> Cliente | None:
    return db.query(Cliente).filter(Cliente.id_cliente == id_cliente).first()

def crear(db: Session, id_cliente: str, nombre: str, telefono: str | None, direccion: str | None) -> Cliente:
    existente = obtener(db, id_cliente)
    if existente:
        raise ValueError("El cliente ya existe")
    c = Cliente(id_cliente=id_cliente, nombre=nombre, telefono=telefono, direccion=direccion)
    db.add(c)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Error al crear cliente")
    db.refresh(c)
    return c

def actualizar(db: Session, id_cliente: str, nombre: str, telefono: str | None, direccion: str | None) -> Cliente:
    c = obtener(db, id_cliente)
    if not c:
        raise ValueError("Cliente no encontrado")
    c.nombre = nombre
    c.telefono = telefono
    c.direccion = direccion
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Error al actualizar cliente")
    db.refresh(c)
    return c

def eliminar(db: Session, id_cliente: str) -> None:
    c = obtener(db, id_cliente)
    if not c:
        raise ValueError("Cliente no encontrado")
    db.delete(c)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Error al eliminar cliente")
