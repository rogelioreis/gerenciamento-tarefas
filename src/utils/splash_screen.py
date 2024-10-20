import time
from conexion.oracle_queries import OracleQueries

class SplashScreen:
    def __init__(self, oracle_queries):
        self.oracle_queries = oracle_queries

    def contar_usuarios(self):
        query = "SELECT COUNT(1) AS total_usuarios FROM USUARIOS"
        result = self.oracle_queries.sqlToMatrix(query)
        return result[0][0][0]  # O primeiro elemento contém o total de usuários

    def contar_tarefas(self):
        query = "SELECT COUNT(1) AS total_tarefas FROM TAREFAS"
        result = self.oracle_queries.sqlToMatrix(query)
        return result[0][0][0]  # O primeiro elemento contém o total de tarefas

    def exibir(self):
        usuarios = self.contar_usuarios()
        tarefas = self.contar_tarefas()

        print("###############################################")
        print("#                                             #")
        print("#      SISTEMA DE GERENCIAMENTO DE TAREFAS    #")
        print("#                                             #")
        print("###############################################")
        print("#                                             #")
        print("#  TOTAL DE REGISTROS EXISTENTES              #")
        print(f"#  1 - USUÁRIOS: {usuarios:<5}")
        print(f"#  2 - TAREFAS: {tarefas:<5}")
        print("#                                             #")
        print("#                                             #")
        print("#  CRIADO POR:                                #")
        print("#  Rogelio Soares Reis Filho                  #")
        print("#  Murilo da Silva Soares Reis                #")
        print("#  Jordhan Fernandes de Assis                 #")
        print("#  Mariana Lopes Ferreira                     #")
        print("#                                             #")
        print("#  DISCIPLINA: BANCO DE DADOS 2024/2          #")
        print("#  PROFESSOR: HOWARD ROATTI                   #")
        print("#                                             #")
        print("###############################################")
        
        # Pausa de 5 segundos para exibir a splash screen
        time.sleep(1)

# Exemplo de chamada no início do programa
if __name__ == "__main__":
    oracle_queries = OracleQueries()
    oracle_queries.connect()  # Conectar ao banco de dados Oracle
    splash_screen = SplashScreen(oracle_queries)  # Criar uma instância de SplashScreen
    splash_screen.exibir()  # Exibir a splash screen com os dados dinâmicos
    oracle_queries.close()  # Fechar a conexão ao banco de dados
