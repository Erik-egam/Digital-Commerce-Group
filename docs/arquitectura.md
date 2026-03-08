# Arquitectura del Proyecto

```mermaid
flowchart TD
    A[main.py FastAPI] --> B[clientes routes]
    A --> C[productos routes]
    A --> D[pedidos routes]

    subgraph Clientes
      B --> S[service clientes]
      S --> E[SQLAlchemy Session get_db]
      S --> O1[ORM Cliente]
      O1 --> DB[(MySQL)]
      B --> M1[Mapper Cliente a JSON]
    end

    subgraph Productos
      C --> O2[ORM Producto]
      O2 --> DB
      C --> M2[Mapper Producto a JSON]
    end

    subgraph Pedidos
      D --> O3[ORM Pedido]
      D --> O4[ORM DetallePedido]
      O3 --> DB
      O4 --> DB
      D --> M3[Mapper Pedido/Detalle a JSON]
    end

    subgraph Configuracion
      E2[sql_alquemy_conexion] --> E
      E2 --> Base[Declarative Base]
      E2 --> ENG[Engine]
      E2 --> Check[check_connection]
    end
```

## Descripción
- Enrutamiento en main.py incluye módulos clientes, productos y pedidos.
- Cada módulo separa la lógica de negocio en service, usando SQLAlchemy y el engine configurado.
- Los mappers convierten objetos ORM a JSON seguro y consistente para las respuestas HTTP.
- La base de datos MySQL se consume sin creación de tablas (ya existentes). 
