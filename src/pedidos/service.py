from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from models.orm.pedido import Pedido
from models.orm.detalle_pedido import DetallePedido
from models.orm.producto import Producto

def listar(db: Session) -> list[Pedido]:
    return db.query(Pedido).all()


def obtener(db: Session, id_pedido: int) -> Pedido | None:
    return db.query(Pedido).filter(Pedido.id_pedido == id_pedido).first()

def crear(db: Session, pedido):

    total = 0
    detalles_db = []

    for item in pedido.detalles:

        producto = db.query(Producto).filter(
            Producto.id_producto == item.id_producto
        ).first()

        if not producto:
            raise ValueError("Producto no encontrado")

        # verificar stock
        if producto.stock < item.cantidad:
            raise ValueError("Stock insuficiente")

        # RESTAR STOCK
        producto.stock -= item.cantidad

        subtotal = producto.precio * item.cantidad
        total += subtotal

        detalle = DetallePedido(
            id_producto=item.id_producto,
            cantidad=item.cantidad,
            subtotal=subtotal
        )

        detalles_db.append(detalle)

    nuevo_pedido = Pedido(
        id_cliente=pedido.id_cliente,
        fecha=datetime.now(),
        total=total,
        estado=pedido.estado,
        metodo_pago=pedido.metodo_pago
    )

    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    for detalle in detalles_db:
        detalle.id_pedido = nuevo_pedido.id_pedido
        db.add(detalle)

    db.commit()

    return nuevo_pedido

def actualizar(db: Session, id_pedido: int, estado: str):

    pedido = db.query(Pedido).filter(
        Pedido.id_pedido == id_pedido
    ).first()

    if not pedido:
        raise ValueError("Pedido no encontrado")

    pedido.estado = estado

    db.commit()
    db.refresh(pedido)

    return pedido

def eliminar(db: Session, id_pedido: int) -> None:

    pedido = obtener(db, id_pedido)

    if not pedido:
        raise ValueError("Pedido no encontrado")

    db.delete(pedido)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Error al eliminar pedido")