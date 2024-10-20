from conexion.oracle_queries import OracleQueries

oracle = OracleQueries(can_write=True)
oracle.connect()

print()

print("Deletando relacionamentos usuarios tarefas...")
oracle.executeDDL("alter table tarefas drop constraint usuarios_tarefas_fk")
print("Relacionamentos deletados com sucesso!")

print()

print("Deletando tabela tarefas...")
oracle.executeDDL("drop table tarefas")
print("Tabela tarefas deletada com sucesso!")

print()

print("Deletando tabela usuarios...")
oracle.executeDDL("drop table usuarios")
print("Tabela usuarios deletada com sucesso!")

print()

print("Deletando Sequencia...")
oracle.executeDDL("drop sequence tarefas_codigo_tarefa_seq")
print("Sequencia deletada com sucesso!")