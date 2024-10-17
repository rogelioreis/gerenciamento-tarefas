import pyodbc


# Configuração da conexão com o SQL Server
def conectar():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=PC-Jordhan;"  # Ajuste conforme o seu servidor
        "Database=LABDATABASE;"  # Nome do banco de dados
        "Trusted_Connection=yes;"  # Se estiver usando autenticação integrada do Windows
    )
    return conn


# Função para inserir usuário
def inserir_usuario():
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO USUARIOS (CPF, NOME)
        VALUES (?, ?)
    """,
        (cpf, nome),
    )

    conn.commit()
    conn.close()
    print("Usuário inserido com sucesso.")


# Função para inserir tarefa
def inserir_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição: ")
    cpf = input("Digite o CPF do usuário: ")
    status = int(input("Digite o status da tarefa (0 ou 1): "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO TAREFAS (TITULO, DESCRICAO, STATUS, CPF)
        VALUES (?, ?, ?, ?)
    """,
        (titulo, descricao, status, cpf),
    )

    conn.commit()
    conn.close()
    print("Tarefa inserida com sucesso.")


# Função para remover usuário
def remover_usuario():
    cpf = input("Digite o CPF do usuário que deseja remover: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USUARIOS WHERE CPF = ?", (cpf,))

    conn.commit()
    conn.close()
    print("Usuário removido com sucesso.")


# Função para remover tarefa
def remover_tarefa():
    codigo_tarefa = int(input("Digite o código da tarefa que deseja remover: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TAREFAS WHERE CODIGO_TAREFA = ?", (codigo_tarefa,))

    conn.commit()
    conn.close()
    print("Tarefa removida com sucesso.")


# Função para atualizar usuário
def atualizar_usuario():
    cpf = input("Digite o CPF do usuário que deseja atualizar: ")
    novo_nome = input("Digite o novo nome: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE USUARIOS SET NOME = ? WHERE CPF = ?", (novo_nome, cpf))

    conn.commit()
    conn.close()
    print("Usuário atualizado com sucesso.")


# Função para atualizar tarefa
def atualizar_tarefa():
    codigo_tarefa = int(input("Digite o código da tarefa que deseja atualizar: "))
    novo_titulo = input("Digite o novo título da tarefa: ")
    nova_descricao = input("Digite a nova descrição: ")
    novo_status = int(input("Digite o novo status da tarefa (0 ou 1): "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE TAREFAS 
        SET TITULO = ?, DESCRICAO = ?, STATUS = ?
        WHERE CODIGO_TAREFA = ?
    """,
        (novo_titulo, nova_descricao, novo_status, codigo_tarefa),
    )

    conn.commit()
    conn.close()
    print("Tarefa atualizada com sucesso.")


# Função para exibir relatórios
def exibir_relatorios():
    conn = conectar()
    cursor = conn.cursor()

    # Relatório 1: Agrupamento (Tarefas por status)
    print("\nRelatório 1: Tarefas por status")
    cursor.execute(
        """
        SELECT STATUS, COUNT(*)
        FROM TAREFAS
        GROUP BY STATUS
    """
    )
    for row in cursor.fetchall():
        print(f"Status: {row[0]}, Total: {row[1]}")

    # Relatório 2: Junção (Tarefas e seus usuários)
    print("\nRelatório 2: Tarefas e seus usuários")
    cursor.execute(
        """
        SELECT U.NOME, T.TITULO, T.STATUS
        FROM USUARIOS U
        JOIN TAREFAS T ON U.CPF = T.CPF
    """
    )
    for row in cursor.fetchall():
        print(f"Usuário: {row[0]}, Tarefa: {row[1]}, Status: {row[2]}")

    conn.close()


# Função principal para o menu
def main():
    while True:
        print("\nMenu Principal")
        print("1. Relatórios")
        print("2. Inserir Registro")
        print("3. Remover Registro")
        print("4. Atualizar Registro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_relatorios()
        elif opcao == "2":
            print("\nMenu de Inserção:")
            print("1. Inserir Usuário")
            print("2. Inserir Tarefa")
            sub_opcao = input("Escolha uma opção: ")
            if sub_opcao == "1":
                inserir_usuario()
            elif sub_opcao == "2":
                inserir_tarefa()
            else:
                print("Opção inválida!")
        elif opcao == "3":
            print("\nMenu de Remoção:")
            print("1. Remover Usuário")
            print("2. Remover Tarefa")
            sub_opcao = input("Escolha uma opção: ")
            if sub_opcao == "1":
                remover_usuario()
            elif sub_opcao == "2":
                remover_tarefa()
            else:
                print("Opção inválida!")
        elif opcao == "4":
            print("\nMenu de Atualização:")
            print("1. Atualizar Usuário")
            print("2. Atualizar Tarefa")
            sub_opcao = input("Escolha uma opção: ")
            if sub_opcao == "1":
                atualizar_usuario()
            elif sub_opcao == "2":
                atualizar_tarefa()
            else:
                print("Opção inválida!")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
