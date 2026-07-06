from src.knowledge import carregar_base_conhecimento


def buscar_resposta(pergunta):

    base = carregar_base_conhecimento()

    pergunta = pergunta.lower()

    for item in base:

        termos = [
            item["categoria"],
            item["problema"]
        ]

        for termo in termos:

            if termo.lower() in pergunta:

                return {
                    "categoria": item["categoria"],
                    "resposta": item["solucao"],
                    "proximo_passo": item["proximo_passo"]
                }

    return {
        "categoria": "Não identificado",
        "resposta": "Não encontrei informações suficientes na minha base de conhecimento.",
        "proximo_passo": "Adicione mais informações ou consulte uma documentação oficial."
    }