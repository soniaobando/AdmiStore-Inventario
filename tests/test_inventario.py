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