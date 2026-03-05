# API Clientes

## Endpoints
- GET /clientes/ — lista todos los clientes
- GET /clientes/{id_cliente} — obtiene un cliente
- POST /clientes/ — crea un cliente
- PUT /clientes/{id_cliente} — actualiza un cliente
- DELETE /clientes/{id_cliente} — elimina un cliente

```mermaid
sequenceDiagram
    participant C as Cliente HTTP
    participant API as FastAPI
    participant S as Service Clientes
    participant DB as MySQL
    participant M as Mapper Cliente

    C->>API: GET /clientes/
    API->>API: get_db abre sesion
    API->>S: listar(db)
    S->>DB: SELECT * FROM Clientes
    DB-->>S: filas
    S-->>API: objetos ORM
    API->>M: map_clientes(items)
    M-->>API: JSON array
    API-->>C: 200 JSON
```

## Ejemplos de Cuerpo para POST/PUT
```json
{
  "id_cliente": "10000021",
  "nombre": "Nuevo Cliente",
  "telefono": "3001234567",
  "direccion": "Calle X #Y-Z"
}
```
