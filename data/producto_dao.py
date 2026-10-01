from data.database import get_connection


class ProductoDAO:

    def crear(self, nombre, precio, stock, stock_minimo):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre, precio, stock, stock_minimo)
            VALUES (?, ?, ?, ?)
        """, (nombre, precio, stock, stock_minimo))

        connection.commit()
        producto_id = cursor.lastrowid
        connection.close()

        return producto_id

    def listar(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, nombre, precio, stock, stock_minimo
            FROM productos
        """)

        productos = cursor.fetchall()
        connection.close()

        return productos

    def actualizar(self, producto_id, nombre, precio, stock, stock_minimo):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE productos
            SET nombre = ?, precio = ?, stock = ?, stock_minimo = ?
            WHERE id = ?
        """, (nombre, precio, stock, stock_minimo, producto_id))

        connection.commit()
        connection.close()

    def eliminar(self, producto_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM productos
            WHERE id = ?
        """, (producto_id,))

        connection.commit()
        connection.close()