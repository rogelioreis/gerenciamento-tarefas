from model.usuarios import Usuario
from conexion.oracle_queries import OracleQueries

class Controller_Usuario:
    def __init__(self):
        pass

    def inserir_usuario(self) -> Usuario:
        ''' Insere um novo usuário na base de dados. '''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuário o novo CPF
        cpf = input("CPF (Novo): ")

        if not self.verifica_existencia_usuario(oracle, cpf):
            # Solicita ao usuário o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo usuário
            oracle.write(f"insert into usuarios values ('{cpf}', '{nome}')")
            # Recupera os dados do novo usuário criado transformando em um DataFrame
            df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
            # Cria um novo objeto Usuario
            novo_usuario = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
            # Exibe os atributos do novo usuário
            print(novo_usuario.to_string())
            # Retorna o objeto novo_usuario para utilização posterior, caso necessário
            return novo_usuario
        else:
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_usuario(self) -> Usuario:
        ''' Atualiza o nome de um usuário existente na base de dados. '''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_usuarios(oracle)

        # Solicita ao usuário o CPF do usuário a ser alterado
        cpf = input("CPF do usuário que deseja alterar o nome: ")

        # Verifica se o usuário existe na base de dados
        if self.verifica_existencia_usuario(oracle, cpf):
            # Solicita a nova descrição do usuário
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do usuário existente
            oracle.write(f"update usuarios set nome = '{novo_nome}' where cpf = '{cpf}'")
            # Recupera os dados do usuário atualizado
            df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
            # Cria um novo objeto Usuario
            usuario_atualizado = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
            # Exibe os atributos do usuário atualizado
            print(usuario_atualizado.to_string())
            # Retorna o objeto usuario_atualizado para utilização posterior, caso necessário
            return usuario_atualizado
        else:
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_usuario(self):
        ''' Exclui um usuário existente na base de dados. '''
        
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_usuarios(oracle)

        # Solicita ao usuário o CPF do usuário a ser excluído
        cpf = input("CPF do Usuário que irá excluir: ")

        # Verifica se o usuário existe na base de dados
        if self.verifica_existencia_usuario(oracle, cpf):
            # Recupera os dados do usuário que será removido
            df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
            # Remove o usuário da tabela
            oracle.write(f"delete from usuarios where cpf = '{cpf}'")
            # Cria um novo objeto Usuario para informar que foi removido
            usuario_excluido = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
            # Exibe os atributos do usuário excluído
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
        ''' Verifica se um usuário já existe na base de dados. '''
        
        # Recupera os dados do usuário criando um DataFrame
        df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = '{cpf}'")
        return not df_usuario.empty
