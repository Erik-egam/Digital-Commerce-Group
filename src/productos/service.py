from sqlalchemy.orm import Session
from models.orm.producto import Producto as ProductoORM

class ProductoService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(ProductoORM).all()

    def get_by_id(self, id_producto: int):
        return self.db.query(ProductoORM).filter(ProductoORM.id_producto == id_producto).first()

    def create(self, datos: dict):
        nuevo_producto = ProductoORM(
            nombre=datos.get("nombre"),
            descripcion=datos.get("descripcion"),
            precio=datos.get("precio"),
            stock=datos.get("stock")
        )
        self.db.add(nuevo_producto)
        self.db.commit()
        self.db.refresh(nuevo_producto)
        return nuevo_producto

    def update(self, id_producto: int, datos: dict):
        producto = self.get_by_id(id_producto)
        if producto:
            for key, value in datos.items():
                setattr(producto, key, value)
            self.db.commit()
            self.db.refresh(producto)
        return producto

    def delete(self, id_producto: int):
        producto = self.get_by_id(id_producto)
        if producto:
            self.db.delete(producto)
            self.db.commit()
            return True
        return False