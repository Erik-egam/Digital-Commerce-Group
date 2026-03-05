from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from config.conexion_mysql import ConexionMySQL

DATABASE_URL = (
    f"mysql+mysqlconnector://{ConexionMySQL.user}:{ConexionMySQL.password}"
    f"@{ConexionMySQL.host}:{ConexionMySQL.port}/{ConexionMySQL.database}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    future=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def check_connection():
    print("Verificando conexión con SQLAlchemy...")
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("Conexión SQLAlchemy exitosa.")
        return True
    except Exception as e:
        print(f"Error de conexión SQLAlchemy: {e}")
        return False

def get_db():
    if not check_connection():
        print("No se puede abrir sesión: conexión fallida.")
    else:
        print("Abriendo sesión SQLAlchemy...")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
