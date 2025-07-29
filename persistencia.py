import json
from datetime import datetime

# Nome do arquivo onde as tarefas serão salvas
ARQUIVO_TAREFAS = "tarefas.json"

def salvar(lista_tarefas):
    # Converte datas para string e salva a lista de tarefas em JSON
    dados = []
    for tarefa in lista_tarefas:
        tarefa_copy = tarefa.copy()
        tarefa_copy["criado_em"] = tarefa["criado_em"].strftime("%d/%m/%Y %H:%M:%S")
        tarefa_copy["atualizado_em"] = tarefa["atualizado_em"].strftime("%d/%m/%Y %H:%M:%S")
        dados.append(tarefa_copy)

    # Escreve os dados formatados no arquivo
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(dados, f, indent=2)

def carregar():
    # Lê o arquivo JSON e converte datas de volta para datetime
    try:
        with open(ARQUIVO_TAREFAS, "r") as f:
            dados = json.load(f)
            for tarefa in dados:
                tarefa["criado_em"] = datetime.strptime(tarefa["criado_em"], "%d/%m/%Y %H:%M:%S")
                tarefa["atualizado_em"] = datetime.strptime(tarefa["atualizado_em"], "%d/%m/%Y %H:%M:%S")
            return dados
    except FileNotFoundError:
        # Retorna lista vazia se o arquivo não existir
        return []