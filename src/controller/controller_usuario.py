from model.usuarios import Usuario # type: ignore
from conexion.oracle_queries import OracleQueries # type: ignore

class Controller_Usuario:
    def __init__(self):
        pass

    def inserir_usuario(self) -> Usuario:
        '''Função para inserir um novo usuário no banco de dados'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF (Novo): ")

        if not self.verifica_existencia_usuario(oracle, cpf):
            nome = input("Nome (Novo): ")

            oracle.write(f"INSERT INTO usuarios (cpf, nome) VALUES ('{cpf}', '{nome}')")

            df_usuario = oracle.sqlToDataFrame(f"SELECT cpf, nome FROM usuarios WHERE cpf = '{cpf}'")

            novo_usuario = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])

            print(novo_usuario.to_string())

            return novo_usuario
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_usuario(self) -> Usuario:
        '''Função para atualizar os dados de um usuário existente'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF do usuário que deseja alterar: ")

        if self.verifica_existencia_usuario(oracle, cpf):
            novo_nome = input("Nome (Novo): ")

            oracle.write(f"UPDATE usuarios SET nome = '{novo_nome}' WHERE cpf = '{cpf}'")

            df_usuario = oracle.sqlToDataFrame(f"SELECT cpf, nome FROM usuarios WHERE cpf = '{cpf}'")

            usuario_atualizado = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])

            print(usuario_atualizado.to_string())

            return usuario_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_usuario(self):
        '''Função para excluir um usuário do banco de dados'''

        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF do usuário que deseja excluir: ")

        if self.verifica_existencia_usuario(oracle, cpf):
            df_usuario = oracle.sqlToDataFrame(f"SELECT cpf, nome FROM usuarios WHERE cpf = '{cpf}'")

            oracle.write(f"DELETE FROM usuarios WHERE cpf = '{cpf}'")

            usuario_excluido = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])

            print("Usuário removido com sucesso!")
            print(usuario_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_usuario(self, oracle: OracleQueries, cpf: str) -> bool:
        '''Função para verificar se o usuário já existe no banco de dados'''
        df_usuario = oracle.sqlToDataFrame(f"SELECT cpf, nome FROM usuarios WHERE cpf = '{cpf}'")

        return not df_usuario.empty
