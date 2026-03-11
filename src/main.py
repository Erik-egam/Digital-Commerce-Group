from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.conexion_mysql import crear_conexion
from clientes import routes as clientes_routes
from productos import routes as productos_routes
from pedidos import routes as pedidos_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes_routes.router, prefix="/clientes")
app.include_router(productos_routes.router, prefix="/productos")
app.include_router(pedidos_routes.router, prefix="/pedidos")

@app.get("/")
def read_root():
    conexion = crear_conexion()
    if conexion:
        print("Conexión exitosa a la base de datos")
        conexion.close()
    else:
        print("Error de conexión a la base de datos")
    return {"Hello": "World"}


