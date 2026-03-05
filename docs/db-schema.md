# Esquema de Base de Datos

```mermaid
erDiagram
    CLIENTES {
        string id_cliente PK
        string nombre
        string telefono
        string direccion
    }
    PRODUCTOS {
        int id_producto PK
        string nombre
        string descripcion
        float precio
        int stock
    }
    PEDIDOS {
        int id_pedido PK
        string id_cliente FK
        datetime fecha
        float total
        string estado
        string metodo_pago
    }
    DETALLE_PEDIDO {
        int id_detalle PK
        int id_pedido FK
        int id_producto FK
        int cantidad
        float subtotal
    }

    CLIENTES ||--o{ PEDIDOS : tiene
    PEDIDOS ||--o{ DETALLE_PEDIDO : contiene
    PRODUCTOS ||--o{ DETALLE_PEDIDO : aparece
```

## Notas
- El campo precio_unitario se eliminó de DetallePedido; se usa subtotal.
- Restricciones: ON DELETE CASCADE en relación Pedidos -> DetallePedido y Clientes -> Pedidos. 
