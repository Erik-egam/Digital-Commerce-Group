from sqlalchemy import Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.sql_alquemy_conexion import Base

class Pedido(Base):
    __tablename__ = "Pedidos"

    id_pedido: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_cliente: Mapped[str] = mapped_column(ForeignKey("Clientes.id_cliente", ondelete="CASCADE", onupdate="CASCADE"))
    fecha: Mapped[str] = mapped_column(DateTime)
    total: Mapped[float] = mapped_column(Numeric(12, 2))
    estado: Mapped[str] = mapped_column(String(20))
    metodo_pago: Mapped[str | None] = mapped_column(String(30), nullable=True)

    cliente = relationship("Cliente", backref="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido", cascade="all, delete-orphan")
