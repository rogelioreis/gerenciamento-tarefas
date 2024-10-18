from conexion.oracle_queries import OracleQueries # type: ignore

class RelatorioUsuarioTarefa:
    def __init__(self):
        with open("sql/relatorio_usuarios.sql") as f:
            self.query_relatorio_usuarios = f.read()

        with open("sql/relatorio_tarefas.sql") as f:
            self.query_relatorio_tarefas = f.read()

        with open("sql/relatorio_usuarios_tarefas.sql") as f:
            self.query_relatorio_usuarios_tarefas = f.read()

    def get_relatorio_usuarios(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_usuarios))
        input("Pressione Enter para Sair do Relatório de Usuários")

    def get_relatorio_tarefas(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_tarefas))
        input("Pressione Enter para Sair do Relatório de Tarefas")

    def get_relatorio_usuarios_tarefas(self):
        oracle = OracleQueries()
        oracle.connect()
        print(oracle.sqlToDataFrame(self.query_relatorio_usuarios_tarefas))
        input("Pressione Enter para Sair do Relatório de Usuários e Tarefas")
