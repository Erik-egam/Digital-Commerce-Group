from sqlalchemy import Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.sql_alquemy_conexion import Base

class DetallePedido(Base):
    __tablename__ = "DetallePedido"

    id_detalle: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_pedido: Mapped[int] = mapped_column(ForeignKey("Pedidos.id_pedido", ondelete="CASCADE"))
    id_producto: Mapped[int] = mapped_column(ForeignKey("Productos.id_producto"))
    cantidad: Mapped[int] = mapped_column(Integer)
    subtotal: Mapped[float] = mapped_column(Numeric(12, 2))

    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto", backref="detalles")
