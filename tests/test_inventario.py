from business.inventario_service import InventarioService


def test_registrar_producto():
    service = InventarioService()

    producto_id = service.registrar_producto(
        "Producto de prueba",
        10.00,
        5,
        2
    )

    assert producto_id is not None


def test_no_permitir_precio_cero():
    service = InventarioService()

    try:
        service.registrar_producto(
            "Producto inválido",
            0,
            5,
            2
        )
        assert False
    except ValueError:
        assert True

def test_eliminar_producto():
    service = InventarioService()

    producto_id = service.registrar_producto(
        "Producto para eliminar",
        15.00,
        3,
        1
    )

    service.eliminar_producto(producto_id)

    productos = service.consultar_productos()

    assert not any(producto[0] == producto_id for producto in productos)