from conexion.oracle_queries import OracleQueries # type: ignore

oracle = OracleQueries(can_write=True)
oracle.connect()

print("Consultando a tabela usuarios:")
result_usuarios_matrix = oracle.sqlToMatrix("SELECT * FROM usuarios")
print(result_usuarios_matrix)

print()

result_usuarios_df = oracle.sqlToDataFrame("SELECT * FROM usuarios")
print(result_usuarios_df)

print()

result_usuarios_json = oracle.sqlToJson("SELECT * FROM usuarios")
print(result_usuarios_json)

print()

print("Consultando a tabela tarefas:")
result_tarefas_matrix = oracle.sqlToMatrix("SELECT * FROM tarefas")
print(result_tarefas_matrix)

print()

result_tarefas_df = oracle.sqlToDataFrame("SELECT * FROM tarefas")
print(result_tarefas_df)

print()

result_tarefas_json = oracle.sqlToJson("SELECT * FROM tarefas")
print(result_tarefas_json)

print()

print("Criando tabela de teste, inserindo valores e consultando:")
oracle.executeDDL("CREATE TABLE test_float (x numeric(5, 3))")
oracle.write("INSERT INTO test_float VALUES (7.1)")
oracle.write("INSERT INTO test_float VALUES (8.4)")

result_test_table = oracle.sqlToDataFrame("SELECT * FROM test_float")
print(result_test_table)

oracle.executeDDL("DROP TABLE test_float")
