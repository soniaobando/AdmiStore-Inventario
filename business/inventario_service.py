from data.producto_dao import ProductoDAO

from data.database import initialize_database


class InventarioService:

   def __init__(self):
    initialize_database()
    self.dao = ProductoDAO()

    def registrar_producto(self, nombre, precio, stock, stock_minimo):
        if not nombre.strip():
            raise ValueError("El nombre del producto es obligatorio.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        if stock_minimo < 0:
            raise ValueError("El stock mínimo no puede ser negativo.")

        return self.dao.crear(
            nombre,
            precio,
            stock,
            stock_minimo
        )

    def consultar_productos(self):
        return self.dao.listar()

    def actualizar_producto(
        self,
        producto_id,
        nombre,
        precio,
        stock,
        stock_minimo
    ):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self.dao.actualizar(
            producto_id,
            nombre,
            precio,
            stock,
            stock_minimo
        )

    def eliminar_producto(self, producto_id):
        self.dao.eliminar(producto_id)

    def verificar_stock_minimo(self, producto):
        return producto[3] <= producto[4]
