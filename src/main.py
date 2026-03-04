from fastapi import FastAPI
from config.conexion_mysql import crear_conexion
from clientes import routes as clientes_routes
from productos import routes as productos_routes
from pedidos import routes as pedidos_routes

app = FastAPI()

app.include_router(clientes_routes.router)
app.include_router(productos_routes.router)
app.include_router(pedidos_routes.router)

@app.get("/")
def read_root():
    conexion = crear_conexion()
    if conexion:
        print("Conexión exitosa a la base de datos")
        conexion.close()
    else:
        print("Error de conexión a la base de datos")
    return {"Hello": "World"}