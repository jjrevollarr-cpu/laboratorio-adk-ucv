from agente_ucv.agent import explicar_concepto


def test_explicar_concepto_existente():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"
    assert "comunicación" in resultado["explicacion"]


def test_explicar_concepto_no_existente():
    resultado = explicar_concepto("concepto_inexistente")
    assert resultado["status"] == "not_found"
    assert resultado["explicacion"] == "Concepto no registrado."