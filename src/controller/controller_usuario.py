from model.usuarios import Usuario
from conexion.oracle_queries import OracleQueries

class Controller_Usuario:
    def __init__(self):
        pass

    def inserir_usuario(self) -> Usuario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        cpf = input("CPF (Novo): ")

        if not self.verifica_existencia_usuario(oracle, cpf):
            nome = input("Nome (Novo): ")
            # Insere
            oracle.write(f"insert into usuarios values ('{cpf}', '{nome}')")
            # Recupera os dados do novo usuário
            df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
            # Cria um novo objeto Usuario
            novo_usuario = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
            # Exibe os atributos do novo usuário
            print("Usuário Inserido com Sucesso!")
            print(novo_usuario.to_string())
            return novo_usuario
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_usuario(self) -> Usuario:
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        self.listar_usuarios(oracle)
        cpf = input("CPF do usuário que deseja alterar o nome: ")

        # Verifica se o usuário existe
        if self.verifica_existencia_usuario(oracle, cpf):
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do usuário existente
            oracle.write(f"update usuarios set nome = '{novo_nome}' where cpf = '{cpf}'")
            # Recupera os dados do usuário atualizado
            df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
            # Cria um novo objeto Usuario
            usuario_atualizado = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
            # Exibe os atributos do usuário atualizado
            print(usuario_atualizado.to_string())
            return usuario_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_usuario(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        self.listar_usuarios(oracle)
        cpf = input("CPF do Usuário que irá excluir: ")

        if self.verifica_existencia_usuario(oracle, cpf):
            if self.verifica_vinculo_tarefa(oracle, cpf):
                print(f"O usuário com CPF {cpf} não pode ser excluído porque está vinculado a uma ou mais tarefas!")
            else:
                df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
                # Remove o usuário da tabela
                oracle.write(f"delete from usuarios where cpf = '{cpf}'")
                usuario_excluido = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
                print("Usuário Removido com Sucesso!")
                print(usuario_excluido.to_string())
        else:
            print(f"O CPF {cpf} não existe.")

    def listar_usuarios(self, oracle: OracleQueries, need_connect: bool = False):
        query = """
                SELECT U.CPF,
                    U.NOME
                    FROM USUARIOS U
                    ORDER BY U.NOME
                """
        if need_connect:
            oracle.connect()

        print(oracle.sqlToDataFrame(query))

    def verifica_existencia_usuario(self, oracle: OracleQueries, cpf: str) -> bool:
        df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
        return not df_usuario.empty
    
    def verifica_vinculo_tarefa(self, oracle: OracleQueries, cpf: str) -> bool:
        query = f"SELECT COUNT(*) FROM tarefas WHERE cpf = '{cpf}'"
        df_tarefas = oracle.sqlToDataFrame(query)
        
        return df_tarefas.iloc[0, 0] > 0 

