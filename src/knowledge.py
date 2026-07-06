import json
import os


def carregar_base_conhecimento():
    """
    Carrega as informações da base de conhecimento.
    """

    caminho = os.path.join(
        "data",
        "knowledge_base.json"
    )

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        print("Base de conhecimento não encontrada.")
        return []

    except json.JSONDecodeError:
        print("Erro ao interpretar a base de conhecimento.")
        return []