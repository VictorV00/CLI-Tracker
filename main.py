# main.py
import argparse
from task import TaskManager

# Inicializa o parser da linha de comando
parser = argparse.ArgumentParser(
    prog="Gerenciador de Tarefas CLI",
    description="Gerencie suas tarefas pelo terminal com Python!"
)

# Define os subcomandos disponíveis
subparser = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

# Comando: adicionar
parser_adicionar = subparser.add_parser("adicionar", help="Adicionar uma nova tarefa")
parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")

# Comando: listar
parser_listar = subparser.add_parser("listar", help="Listar todas as tarefas")

# Comando: remover
parser_remover = subparser.add_parser("remover", help="Remover uma tarefa pelo ID")
parser_remover.add_argument("id", type=int, help="ID da tarefa que será removida")

# Comando: atualizar
parser_atualizar = subparser.add_parser("atualizar", help="Atualizar a descrição de uma tarefa")
parser_atualizar.add_argument("id", type=int, help="ID da tarefa")
parser_atualizar.add_argument("descricao", type=str, help="Nova descrição")

# Comando: atualizar-status
parser_status = subparser.add_parser("atualizar-status", help="Atualizar o status da tarefa")
parser_status.add_argument("id", type=int, help="ID da tarefa")
parser_status.add_argument("status", type=str, choices=["a-fazer", "em-progresso", "concluída"], help="Novo status")

# Comando: listar-status
parser_listar_status = subparser.add_parser("listar-status", help="Listar tarefas com base no status")
parser_listar_status.add_argument("status", type=str, choices=["a-fazer", "em-progresso", "concluída"], help="Status para filtrar")

# Parse dos argumentos
args = parser.parse_args()

# Execução dos comandos
if args.comando == "adicionar":
    TaskManager(args.descricao)

elif args.comando == "listar":
    TaskManager.listar()

elif args.comando == "remover":
    TaskManager.deletar(args.id)

elif args.comando == "atualizar":
    TaskManager.atualizar(args.id, args.descricao)

elif args.comando == "atualizar-status":
    TaskManager.progresso_tarefa(args.id, args.status)

elif args.comando == "listar-status":
    TaskManager.listar_por_status(args.status)
