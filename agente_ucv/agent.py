import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent

load_dotenv()


def explicar_concepto(concepto: str) -> dict:
    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
    }
    concepto = concepto.lower().strip()
    if concepto in conceptos:
        return {"status": "success", "explicacion": conceptos[concepto]}
    return {"status": "not_found", "explicacion": "Concepto no registrado."}


root_agent = Agent(
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="""
    Eres un asistente académico.
    Responde en español.
    Usa lenguaje simple.
    """,
    tools=[explicar_concepto],
)