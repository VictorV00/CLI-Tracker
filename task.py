from datetime import datetime
import persistencia  # Importa módulo responsável por salvar/carregar tarefas

class TaskManager:
    # Carrega tarefas existentes do arquivo
    lista_tarefas = persistencia.carregar()
    # Define o último ID com base nas tarefas existentes
    ultimo_id = max((t["id"] for t in lista_tarefas), default=0)

    def __init__(self, descricao, status='a-fazer'):
        # Cria nova tarefa com ID e data atual
        TaskManager.ultimo_id += 1
        data = datetime.now()
        nova_tarefa = {
            "id": TaskManager.ultimo_id,
            "descricao": descricao,
            "status": status,
            "criado_em": data,
            "atualizado_em": data
        }
        # Adiciona à lista e salva no arquivo
        TaskManager.lista_tarefas.append(nova_tarefa)
        persistencia.salvar(TaskManager.lista_tarefas)
        print("Tarefa cadastrada!")

    @classmethod
    def listar(cls):
        # Lista todas as tarefas salvas
        cls.lista_tarefas = persistencia.carregar()
        if not cls.lista_tarefas:
            print("Lista Vazia!")
            return
        for tarefa in cls.lista_tarefas:
            print(f"ID: {tarefa['id']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Status: {tarefa['status']}")
            print(f"Criado em: {tarefa['criado_em'].strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Atualizado em: {tarefa['atualizado_em'].strftime('%d/%m/%Y %H:%M:%S')}")
            print("-" * 50)

    @classmethod
    def deletar(cls, idtarefa):
        # Remove uma tarefa pelo ID
        cls.lista_tarefas = persistencia.carregar()
        for index, tarefa in enumerate(cls.lista_tarefas):
            if tarefa["id"] == idtarefa:
                del cls.lista_tarefas[index]
                persistencia.salvar(cls.lista_tarefas)
                print("Tarefa deletada!")
                return
        print("Tarefa não encontrada!")

    @classmethod
    def atualizar(cls, idtarefa, descricao):
        # Atualiza a descrição de uma tarefa
        cls.lista_tarefas = persistencia.carregar()
        for tarefa in cls.lista_tarefas:
            if tarefa["id"] == idtarefa:
                tarefa["descricao"] = descricao
                tarefa["atualizado_em"] = datetime.now()
                persistencia.salvar(cls.lista_tarefas)
                print(f"Tarefa ID {idtarefa} atualizada com sucesso!")
                return
        print(f"Tarefa com ID {idtarefa} não encontrada!")

    @classmethod
    def progresso_tarefa(cls, idtarefa, status):
        # Atualiza o status de uma tarefa
        cls.lista_tarefas = persistencia.carregar()
        for tarefa in cls.lista_tarefas:
            if tarefa["id"] == idtarefa:
                tarefa["status"] = status
                tarefa["atualizado_em"] = datetime.now()
                persistencia.salvar(cls.lista_tarefas)
                print(f"Status da tarefa ID {idtarefa} atualizado para {status}")
                return
        print("Tarefa não encontrada!")

    @classmethod
    def listar_por_status(cls, status):
        # Lista apenas tarefas com o status especificado
        cls.lista_tarefas = persistencia.carregar()
        for tarefa in cls.lista_tarefas:
            if tarefa["status"] == status:
                print(f"ID: {tarefa['id']} | Descrição: {tarefa['descricao']} | Status: {tarefa['status']}")
