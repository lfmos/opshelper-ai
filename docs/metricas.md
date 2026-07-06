# Avaliação e Métricas - OpsHelper AI

## Objetivo da avaliação

A avaliação do OpsHelper AI tem como objetivo verificar se o assistente consegue encontrar informações relevantes na base de conhecimento, responder dúvidas relacionadas ao seu domínio e evitar respostas sem fundamento.

---

# Metodologia de teste

Foram realizados testes simulando situações comuns encontradas em ambientes de infraestrutura e DevOps.

Cada teste avaliou:

* capacidade de identificar o assunto;
* qualidade da orientação fornecida;
* indicação de próximos passos;
* comportamento quando a informação não está disponível.

---

# Casos de teste

| Teste | Pergunta realizada                                   | Resultado esperado                                  |
| ----- | ---------------------------------------------------- | --------------------------------------------------- |
| 1     | Minha chave SSH apresenta permission denied          | Encontrar orientação relacionada a SSH e permissões |
| 2     | Não consigo acessar minha instância EC2              | Encontrar possíveis causas de acesso AWS            |
| 3     | Meu container Docker parou                           | Apresentar comandos de diagnóstico Docker           |
| 4     | Minha aplicação não responde em uma porta específica | Indicar análise de rede e firewall                  |
| 5     | Como alterar permissão de arquivos Linux             | Apresentar orientação sobre chmod e permissões      |
| 6     | Como configurar uma impressora residencial           | Informar que não possui conhecimento suficiente     |

---

# Resultado da avaliação

Durante os testes realizados, o assistente apresentou respostas adequadas para situações presentes na sua base de conhecimento.

Quando uma solicitação estava fora do escopo definido, o sistema informou que não possuía informações suficientes, evitando respostas inventadas.

---

# Melhorias futuras

Algumas melhorias planejadas para versões futuras:

* utilização de modelos de linguagem mais avançados;
* implementação de busca semântica;
* integração com APIs de Inteligência Artificial;
* criação de interface web;
* armazenamento de histórico das conversas.

---

# Conclusão

Os testes demonstraram que o OpsHelper AI consegue atuar como uma ferramenta inicial de apoio técnico, auxiliando usuários na compreensão de problemas comuns de infraestrutura e direcionando possíveis caminhos de solução.
