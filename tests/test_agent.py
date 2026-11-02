import sys
from unittest.mock import MagicMock

# Interceptar la inicialización de Google ADK antes de importar el módulo
sys.modules["google.adk.agents.llm_agent"] = MagicMock()

from agente_ucv.agent import explicar_concepto


def test_explicar_concepto_exito():
    resultado = explicar_concepto("api")
    assert resultado["status"] == "success"
    assert "comunicación" in resultado["explicacion"]


def test_explicar_concepto_no_encontrado():
    resultado = explicar_concepto("desconocido")
    assert resultado["status"] == "not_found"