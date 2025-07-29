
# Gerenciador de Tarefas CLI

Projeto simples de linha de comando em Python para gerenciar tarefas com persistência em arquivo JSON.

## Funcionalidades

- Adicionar uma nova tarefa
- Listar todas as tarefas
- Filtrar tarefas por status
- Atualizar descrição
- Atualizar status
- Remover tarefas

## Como usar

1. **Clone o repositório:**

```bash
git clone https://github.com/VictorV00/CLI-TRACKER.git
cd gerenciador-tarefas-cli
```

2. **Execute os comandos:**

```bash
python main.py adicionar "Estudar Python"
python main.py listar
python main.py atualizar 1 "Estudar Python e praticar"
python main.py atualizar-status 1 concluída
python main.py listar-status a-fazer
python main.py remover 1
```

## Status disponíveis

- `a-fazer`
- `em-progresso`
- `concluída`

##Estrutura do projeto

```
.
├── main.py           # Interface CLI
├── task.py           # Regras de negócio
├── persistencia.py   # Leitura e gravação em JSON
├── tarefas.json      # Arquivo gerado automaticamente
└── README.md         # Este documento
```

## Ideias futuras

- [ ] Interface web com Flask ou FastAPI
- [ ] Integração com banco de dados SQLite
- [ ] Suporte a prazos e prioridades

##Licença

Este projeto é open-source e livre para uso pessoal ou educacional. Licença [MIT](https://opensource.org/licenses/MIT).
