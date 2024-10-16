from utils import config
from utils.splash_screen import SplashScreen # type: ignore
from controller.controller_usuario import Controller_Usuario
from controller.controller_tarefa import Controller_Tarefa # type: ignore

# Inicializa as classes
tela_inicial = SplashScreen()
ctrl_usuario = Controller_Usuario()
ctrl_tarefa = Controller_Tarefa()

# Funções para relatórios
def reports(opcao_relatorio:int=0):
    if opcao_relatorio == 1:
        print("Relatório de Usuários")
        # Implemente a lógica para mostrar relatório de usuários
    elif opcao_relatorio == 2:
        print("Relatório de Tarefas")
        # Implemente a lógica para mostrar relatório de tarefas

# Funções para inserir dados
def inserir(opcao_inserir:int=0):
    if opcao_inserir == 1:
        ctrl_usuario.inserir_usuario()
    elif opcao_inserir == 2:
        ctrl_tarefa.inserir_tarefa()

# Funções para atualizar dados
def atualizar(opcao_atualizar:int=0):
    if opcao_atualizar == 1:
        ctrl_usuario.atualizar_usuario()
    elif opcao_atualizar == 2:
        ctrl_tarefa.atualizar_tarefa()

# Funções para excluir dados
def excluir(opcao_excluir:int=0):
    if opcao_excluir == 1:
        ctrl_usuario.excluir_usuario()
    elif opcao_excluir == 2:
        ctrl_tarefa.excluir_tarefa()

# Função principal
def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1:  # Relatórios
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-2]: "))
            config.clear_console(1)
            reports(opcao_relatorio)
            config.clear_console(1)

        elif opcao == 2:  # Inserir Novos Registros
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)
            inserir(opcao_inserir=opcao_inserir)
            config.clear_console()

        elif opcao == 3:  # Atualizar Registros
            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)
            atualizar(opcao_atualizar=opcao_atualizar)
            config.clear_console()

        elif opcao == 4:  # Excluir Registros
            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-2]: "))
            config.clear_console(1)
            excluir(opcao_excluir=opcao_excluir)
            config.clear_console()

        elif opcao == 5:  # Sair
            print(tela_inicial.get_updated_screen())
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
