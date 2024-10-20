from conexion.oracle_queries import OracleQueries

def criar_tabelas(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Successfully executed")
            except Exception as e:
                print(e)            

def inserir_registros(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Successfully executed")

def run():

    # Arquivo SQL para criação das tabelas de usuários e tarefas
    with open("../sql/criar_tabelas_tarefas.sql") as f:
        query_criar = f.read()

    print("Criando tabelas...")
    criar_tabelas(query=query_criar)
    print("Tabelas criadas com sucesso!")

    # Arquivo SQL para inserir registros de usuários e tarefas
    with open("../sql/inserir_registros_tabelas.sql") as f:
        query_inserir_registros = f.read()

    print("Inserindo registros...")
    inserir_registros(query=query_inserir_registros)
    print("Registros inseridos com sucesso!")

if __name__ == '__main__':
    run()
