# 🤖 OpsHelper AI - Assistente Virtual para Infraestrutura e DevOps

Assistente virtual desenvolvido em Python para auxiliar estudantes e profissionais iniciantes na resolução de dúvidas relacionadas à infraestrutura, Linux, Docker, AWS, Git, SSH e redes.

Projeto desenvolvido como parte do desafio **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da DIO, com foco na organização de conhecimento, engenharia de prompts e desenvolvimento de aplicações em Python.

---

# 📖 Sobre o projeto

O OpsHelper AI foi criado para atuar como um assistente técnico capaz de consultar uma base de conhecimento própria e fornecer orientações sobre problemas comuns encontrados em ambientes de infraestrutura.

O objetivo é oferecer respostas claras, organizadas e confiáveis, auxiliando no diagnóstico inicial de situações recorrentes da área de TI.

---

# 🎯 Objetivos

- Auxiliar estudantes e profissionais iniciantes;
- Organizar informações técnicas em uma base de conhecimento;
- Demonstrar conceitos de Assistentes Virtuais utilizando IA;
- Evitar respostas inventadas quando não houver informação disponível.

---

# 🚀 Funcionalidades

- Consulta de uma base de conhecimento em JSON;
- Busca inteligente por palavras-chave;
- Respostas organizadas por categoria;
- Sugestão de próximos passos para resolução de problemas;
- Tratamento de perguntas fora do escopo do assistente.

---

# 🛠️ Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub
- Engenharia de Prompts

---

# 📂 Estrutura do projeto

```text
opshelper-ai/

├── data/
│   └── knowledge_base.json

├── docs/
│   ├── documentacao.md
│   ├── metricas.md
│   ├── pitch.md
│   └── prompt.md

├── src/
│   ├── assistant.py
│   └── knowledge.py

├── app.py
├── README.md
├── requirements.txt
└── LICENSE
```

---

# ▶️ Como executar

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
```

Acesse a pasta do projeto:

```bash
cd opshelper-ai
```

Execute a aplicação:

```bash
python app.py
```

---

# 💬 Exemplo de uso

```text
Usuário:
Minha chave SSH apresenta erro de permissão.

OpsHelper AI:

Categoria: SSH

Orientação:
Verifique se a chave privada possui as permissões corretas utilizando chmod 400.

Próximo passo:
Confirme o usuário utilizado na conexão e valide as regras de acesso da instância.
```

---

# 📈 Melhorias futuras

- Integração com modelos de IA (Gemini ou OpenAI);
- Interface web;
- Busca semântica;
- Expansão da base de conhecimento;
- Histórico de conversas.

---

# 📚 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

- Estruturação de bases de conhecimento;
- Engenharia de prompts;
- Organização de projetos Python;
- Tratamento de dados em JSON;
- Desenvolvimento de assistentes virtuais.

---

# 👨‍💻 Autor

Desenvolvido por **Luis Filipe Medeiros** como projeto de estudo e portfólio.