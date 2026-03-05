from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from config.sql_alquemy_conexion import Base

class Producto(Base):
    __tablename__ = "Productos"

    id_producto: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100))
    descripcion: Mapped[str | None] = mapped_column(String(300), nullable=True)
    precio: Mapped[float] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(Integer)
