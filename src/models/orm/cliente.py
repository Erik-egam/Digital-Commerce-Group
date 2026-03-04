from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from config.sql_alquemy_conexion import Base

class Cliente(Base):
    __tablename__ = "Clientes"

    id_cliente: Mapped[str] = mapped_column(String(20), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str | None] = mapped_column(String(20), nullable=True)
    direccion: Mapped[str | None] = mapped_column(String(200), nullable=True)
