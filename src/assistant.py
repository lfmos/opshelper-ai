"""
OpsHelper AI

Módulo responsável pela lógica do assistente.

Este arquivo recebe a pergunta do usuário, consulta a base de
conhecimento e retorna a resposta mais adequada com base nas
palavras-chave identificadas.
"""

from src.knowledge import carregar_base_conhecimento


def encontrar_palavras_chave(texto):

    palavras = texto.lower().split()

    palavras_remover = [
        "o",
        "a",
        "os",
        "as",
        "um",
        "uma",
        "como",
        "meu",
        "minha",
        "não",
        "nao",
        "está",
        "esta"
    ]

    return [
        palavra
        for palavra in palavras
        if palavra not in palavras_remover
    ]


def buscar_resposta(pergunta):

    base = carregar_base_conhecimento()

    palavras_usuario = encontrar_palavras_chave(pergunta)


    melhor_resultado = None
    maior_pontuacao = 0


    for item in base:

        texto_base = (
            item["categoria"]
            + " "
            + item["problema"]
        ).lower()


        pontuacao = 0


        for palavra in palavras_usuario:

            if palavra in texto_base:
                pontuacao += 1


        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_resultado = item


    if melhor_resultado and maior_pontuacao > 0:

        return {
            "categoria": melhor_resultado["categoria"],
            "resposta": melhor_resultado["solucao"],
            "proximo_passo": melhor_resultado["proximo_passo"]
        }


    return {
        "categoria": "Não identificado",
        "resposta": "Não encontrei informações suficientes na minha base de conhecimento.",
        "proximo_passo": "Adicione mais informações ou consulte uma documentação oficial."
    }