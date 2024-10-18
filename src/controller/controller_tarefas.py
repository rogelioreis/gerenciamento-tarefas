from model.tarefas import Tarefa
from conexion.oracle_queries import OracleQueries # type: ignore

class Controller_Tarefa:
    def __init__(self):
        pass

    def inserir_tarefa(self) -> Tarefa:
        '''Função para inserir uma nova tarefa no banco de dados'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        titulo = input("Título da Tarefa: ")
        descricao = input("Descrição: ")
        cpf = input("CPF do usuário responsável: ")
        status = int(input("Status da tarefa (0 = Incompleta, 1 = Completa): "))

        if self.verifica_existencia_usuario(oracle, cpf):
            oracle.write(f"""
                INSERT INTO tarefas (titulo, descricao, data_criacao, status, cpf)
                VALUES ('{titulo}', '{descricao}', SYSTIMESTAMP, {status}, '{cpf}')
            """)

            df_tarefa = oracle.sqlToDataFrame(f"SELECT codigo_tarefa, titulo, descricao, data_criacao, status, cpf FROM tarefas WHERE cpf = '{cpf}' AND titulo = '{titulo}'")

            nova_tarefa = Tarefa(df_tarefa.codigo_tarefa.values[0], df_tarefa.titulo.values[0], df_tarefa.descricao.values[0], df_tarefa.data_criacao.values[0], df_tarefa.status.values[0], df_tarefa.cpf.values[0])

            print(nova_tarefa.to_string())

            return nova_tarefa
        else:
            print(f"O CPF {cpf} não existe na tabela USUARIOS.")
            return None

    def atualizar_tarefa(self) -> Tarefa:
        '''Função para atualizar uma tarefa existente no banco de dados'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_tarefa = int(input("Código da Tarefa que deseja alterar: "))

        if self.verifica_existencia_tarefa(oracle, codigo_tarefa):
            novo_titulo = input("Novo Título: ")
            nova_descricao = input("Nova Descrição: ")
            novo_status = int(input("Novo Status (0 = Incompleta, 1 = Completa): "))

            oracle.write(f"""
                UPDATE tarefas
                SET titulo = '{novo_titulo}', descricao = '{nova_descricao}', status = {novo_status}, data_conclusao = CASE WHEN {novo_status} = 1 THEN SYSTIMESTAMP ELSE NULL END
                WHERE codigo_tarefa = {codigo_tarefa}
            """)

            df_tarefa = oracle.sqlToDataFrame(f"SELECT codigo_tarefa, titulo, descricao, data_criacao, data_conclusao, status, cpf FROM tarefas WHERE codigo_tarefa = {codigo_tarefa}")

            tarefa_atualizada = Tarefa(df_tarefa.codigo_tarefa.values[0], df_tarefa.titulo.values[0], df_tarefa.descricao.values[0], df_tarefa.data_criacao.values[0], df_tarefa.status.values[0], df_tarefa.cpf.values[0], df_tarefa.data_conclusao.values[0])

            print(tarefa_atualizada.to_string())

            return tarefa_atualizada
        else:
            print(f"O código da tarefa {codigo_tarefa} não existe.")
            return None

    def excluir_tarefa(self):
        '''Função para excluir uma tarefa do banco de dados'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        codigo_tarefa = int(input("Código da Tarefa que deseja excluir: "))

        if self.verifica_existencia_tarefa(oracle, codigo_tarefa):
            df_tarefa = oracle.sqlToDataFrame(f"SELECT codigo_tarefa, titulo, descricao, cpf FROM tarefas WHERE codigo_tarefa = {codigo_tarefa}")

            oracle.write(f"DELETE FROM tarefas WHERE codigo_tarefa = {codigo_tarefa}")

            tarefa_excluida = Tarefa(df_tarefa.codigo_tarefa.values[0], df_tarefa.titulo.values[0], df_tarefa.descricao.values[0], None, None, df_tarefa.cpf.values[0])

            print("Tarefa removida com sucesso!")
            print(tarefa_excluida.to_string())
        else:
            print(f"O código da tarefa {codigo_tarefa} não existe.")

    def verifica_existencia_usuario(self, oracle: OracleQueries, cpf: str) -> bool:
        '''Verifica se o usuário responsável pela tarefa existe no banco de dados'''
        df_usuario = oracle.sqlToDataFrame(f"SELECT cpf FROM usuarios WHERE cpf = '{cpf}'")
        return not df_usuario.empty

    def verifica_existencia_tarefa(self, oracle: OracleQueries, codigo_tarefa: int) -> bool:
        '''Verifica se a tarefa existe no banco de dados'''
        df_tarefa = oracle.sqlToDataFrame(f"SELECT codigo_tarefa FROM tarefas WHERE codigo_tarefa = {codigo_tarefa}")
        return not df_tarefa.empty
