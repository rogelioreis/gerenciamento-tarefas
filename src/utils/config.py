def clear_console(wait_time:int=4):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")

# Mensagens de menu
MENU_PRINCIPAL = """
Bem-vindo ao Sistema de Gerenciamento de Tarefas
1 - Relatórios
2 - Inserir Novos Registros
3 - Atualizar Registros
4 - Excluir Registros
5 - Sair
"""

MENU_RELATORIOS = """
Escolha uma opção de relatório:
1 - Relatório de Usuários
2 - Relatório de Tarefas
3 - Relatório de Tarefas Concluídas
0 - Voltar
"""

MENU_ENTIDADES = """
Escolha uma opção de entidade:
1 - Usuários
2 - Tarefas
"""
