"""
OpsHelper AI

Arquivo principal da aplicação.

Responsável por iniciar a interação entre o usuário
e o assistente virtual.
"""

from src.assistant import buscar_resposta


def iniciar_assistente():

    print("=" * 50)
    print("🤖 OpsHelper AI - Assistente de Infraestrutura")
    print("=" * 50)

    print("\nDigite sua dúvida técnica.")
    print("Digite 'sair' para encerrar.\n")


    while True:

        pergunta = input("Usuário: ")

        if pergunta.lower() == "sair":
            print("\nEncerrando OpsHelper AI. Até mais!")
            break


        resposta = buscar_resposta(pergunta)


        print("\nOpsHelper AI:")
        print(f"Categoria: {resposta['categoria']}")
        print(f"\nOrientação: {resposta['resposta']}")
        print(f"\nPróximo passo: {resposta['proximo_passo']}")
        print("-" * 50)



if __name__ == "__main__":
    iniciar_assistente()