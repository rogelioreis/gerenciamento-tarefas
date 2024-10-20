from model.tarefas import Tarefa
from model.usuarios import Usuario
from controller.controller_usuario import Controller_Usuario
from conexion.oracle_queries import OracleQueries
from datetime import datetime

class Controller_Tarefa:
    def __init__(self):
        self.ctrl_usuario = Controller_Usuario()

    def inserir_tarefa(self) -> Tarefa:
        oracle = OracleQueries()
        
        # Lista os usuários
        self.listar_usuarios(oracle, need_connect=True)
        usuario_cpf = str(input("Digite o CPF do Usuário responsável pela tarefa: "))
        usuario = self.valida_usuario(oracle, usuario_cpf)
        if usuario is None:
            return None
        
        titulo = str(input("Digite o titulo da tarefa: "))
        descricao = str(input("Digite a descrição da tarefa: "))
        data_criacao = datetime.now()

        # Recupera o cursor para executar um bloco PL/SQL 
        cursor = oracle.connect()
        # Cria a variável de saída com o tipo especificado
        output_value = cursor.var(int)

        # Cria um dicionário para mapear as variáveis de entrada e saída
        data = dict(codigo=output_value, titulo=titulo, descricao=descricao, data_criacao=data_criacao, usuario_cpf=usuario.get_CPF())
        
        # Executa o bloco PL/SQL anônimo para inserção da nova tarefa e recuperação da chave primária
        cursor.execute("""
        begin
            :codigo := TAREFAS_CODIGO_TAREFA_SEQ.NEXTVAL;
            insert into tarefas (codigo_tarefa, titulo, descricao, data_criacao, cpf) values(:codigo, :titulo, :descricao, :data_criacao, :usuario_cpf);
        end;
        """, data)
        
        codigo_tarefa = output_value.getvalue()

        # Confirma as alterações
        oracle.conn.commit()

        df_tarefa = oracle.sqlToDataFrame(f"select codigo_tarefa, titulo, descricao, data_criacao from tarefas where codigo_tarefa = {codigo_tarefa}")

        nova_tarefa = Tarefa(
            codigo_tarefa=df_tarefa.codigo_tarefa.values[0],
            titulo=df_tarefa.titulo[0],
            descricao=df_tarefa.descricao.values[0],
            data_criacao=df_tarefa.data_criacao.values[0],
            usuario=usuario
        )
        
        print(nova_tarefa.to_string())
        
        return nova_tarefa

    def atualizar_tarefa(self) -> Tarefa:
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_tarefas(oracle)

        codigo_tarefa = int(input("Código da Tarefa que irá alterar: "))        

        # Verifica se a tarefa existe
        if self.verifica_existencia_tarefa(oracle, codigo_tarefa):

            df_tarefa = oracle.sqlToDataFrame(f"select codigo_tarefa, titulo, descricao, data_criacao, status from tarefas where codigo_tarefa = {codigo_tarefa}")

            tarefa_atual = Tarefa(
                codigo_tarefa=df_tarefa.codigo_tarefa.values[0],
                titulo=df_tarefa.titulo[0],
                descricao=df_tarefa.descricao.values[0],
                data_criacao=df_tarefa.data_criacao.values[0],
                status=df_tarefa.status.values[0],
            )

            # Verifica se a tarefa está concluída
            if tarefa_atual.get_status() == 1:
                print("Não é possível atualizar uma tarefa que já foi concluída.")
                return None  

            print("1 - Alterar dados")
            print("2 - Concluir tarefa")
            print("0 - Sair")
            escolha = int(input("Escolha uma opcao [0 - 2]: "))

            print()

            if escolha == 1:
                self.listar_usuarios(oracle)
                usuario_cpf = str(input("Digite o CPF do Usuário responsável pela tarefa: "))
                usuario = self.valida_usuario(oracle, usuario_cpf)

                if usuario is None:
                    return None

                novo_titulo = str(input("Digite o novo titulo da tarefa: "))
                nova_descricao = str(input("Digite a nova descrição da tarefa: "))
                
                data_criacao = datetime.now()
                data_criacao_str = data_criacao.strftime('%Y-%m-%d %H:%M:%S')

                # Atualiza a descrição
                oracle.write(f"update tarefas set titulo = '{novo_titulo}', descricao = '{nova_descricao}', data_criacao = to_date('{data_criacao_str}', 'yyyy-mm-dd hh24:mi:ss'), cpf = '{usuario.get_CPF()}' where codigo_tarefa = {codigo_tarefa}")

                df_tarefa = oracle.sqlToDataFrame(f"select codigo_tarefa, titulo, descricao, data_criacao from tarefas where codigo_tarefa = {codigo_tarefa}")
                
                tarefa_atualizada = Tarefa(
                    codigo_tarefa=df_tarefa.codigo_tarefa.values[0],
                    titulo=df_tarefa.titulo[0],
                    descricao=df_tarefa.descricao.values[0],
                    data_criacao=df_tarefa.data_criacao.values[0],
                    usuario=usuario
                )

                print(tarefa_atualizada.to_string())
                
                return tarefa_atualizada
            
            elif escolha == 2:
                data_conclusao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Atualizando o status da tarefa para 'concluída' e registrando a data de conclusão
                oracle.write(f"update tarefas set status = 1, data_conclusao = to_timestamp('{data_conclusao}', 'yyyy-mm-dd hh24:mi:ss') where codigo_tarefa = {codigo_tarefa}")
                
                df_tarefa = oracle.sqlToDataFrame(f"select codigo_tarefa, titulo, descricao, data_criacao, data_conclusao, cpf from tarefas where codigo_tarefa = {codigo_tarefa}")

                usuario_cpf = df_tarefa.cpf.values[0]
                usuario = self.valida_usuario(oracle, usuario_cpf)

                tarefa_atualizada = Tarefa(
                    codigo_tarefa=df_tarefa.codigo_tarefa.values[0],
                    titulo=df_tarefa.titulo.values[0],
                    descricao=df_tarefa.descricao.values[0],
                    data_criacao=df_tarefa.data_criacao.values[0],
                    status=1,
                    usuario=usuario
                )

                print(tarefa_atualizada.to_string())
                
                return tarefa_atualizada

            else:
                return None
        else:
            print(f"O código {codigo_tarefa} não existe.")
            return None

    def excluir_tarefa(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        self.listar_tarefas(oracle)

        codigo_tarefa = int(input("Código da Tarefa que irá excluir: "))        

        # Verifica se a tarefa existe
        if self.verifica_existencia_tarefa(oracle, codigo_tarefa):
            opcao_excluir = input(f"Tem certeza que deseja excluir a tarefa {codigo_tarefa} [S ou N]: ")
            if opcao_excluir.lower() == "s":
                # Remove a tarefa
                oracle.write(f"delete from tarefas where codigo_tarefa = {codigo_tarefa}")
                print("Tarefa removida com sucesso!")
        else:
            print(f"O código {codigo_tarefa} não existe.")

    def verifica_existencia_tarefa(self, oracle: OracleQueries, codigo: int) -> bool:
        df_tarefa = oracle.sqlToDataFrame(f"select codigo_tarefa from tarefas where codigo_tarefa = {codigo}")
        return not df_tarefa.empty

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

    def listar_tarefas(self, oracle: OracleQueries, need_connect: bool = False):
        query = """
                SELECT T.CODIGO_TAREFA,
                    T.TITULO,
                    T.DESCRICAO,
                    T.DATA_CRIACAO,
                    T.DATA_CONCLUSAO,
                    CASE 
                        WHEN T.STATUS = 0 THEN 'Pendente'
                        WHEN T.STATUS = 1 THEN 'Concluída'
                        ELSE 'Outro'
                    END AS STATUS,
                    T.CPF
                    FROM TAREFAS T
                    ORDER BY T.DATA_CRIACAO
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_usuario(self, oracle: OracleQueries, usuario_cpf: str) -> Usuario:
        if not self.ctrl_usuario.verifica_existencia_usuario(oracle, usuario_cpf):
            print(f"O CPF {usuario_cpf} informado não existe na base.")
            return None
        else:
            oracle.connect()
            df_usuario = oracle.sqlToDataFrame(f"select cpf, nome from usuarios where cpf = {usuario_cpf}")
            usuario = Usuario(df_usuario.cpf.values[0], df_usuario.nome.values[0])
            return usuario
