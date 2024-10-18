class Tarefa:
    def __init__(self, 
                 codigo_tarefa: int = None, 
                 titulo: str = None, 
                 descricao: str = None, 
                 data_criacao: str = None, 
                 status: int = None, 
                 cpf: str = None, 
                 data_conclusao: str = None):
        self.set_codigo_tarefa(codigo_tarefa)
        self.set_titulo(titulo)
        self.set_descricao(descricao)
        self.set_data_criacao(data_criacao)
        self.set_status(status)
        self.set_cpf(cpf)
        self.set_data_conclusao(data_conclusao)

    def set_codigo_tarefa(self, codigo_tarefa: int):
        self.codigo_tarefa = codigo_tarefa

    def set_titulo(self, titulo: str):
        self.titulo = titulo

    def set_descricao(self, descricao: str):
        self.descricao = descricao

    def set_data_criacao(self, data_criacao: str):
        self.data_criacao = data_criacao

    def set_status(self, status: int):
        self.status = status

    def set_cpf(self, cpf: str):
        self.cpf = cpf

    def set_data_conclusao(self, data_conclusao: str):
        self.data_conclusao = data_conclusao

    def get_codigo_tarefa(self) -> int:
        return self.codigo_tarefa

    def get_titulo(self) -> str:
        return self.titulo

    def get_descricao(self) -> str:
        return self.descricao

    def get_data_criacao(self) -> str:
        return self.data_criacao

    def get_status(self) -> int:
        return self.status

    def get_cpf(self) -> str:
        return self.cpf

    def get_data_conclusao(self) -> str:
        return self.data_conclusao

    def to_string(self) -> str:
        return (f"Código Tarefa: {self.get_codigo_tarefa()} | "
                f"Título: {self.get_titulo()} | "
                f"Descrição: {self.get_descricao()} | "
                f"Data Criação: {self.get_data_criacao()} | "
                f"Data Conclusão: {self.get_data_conclusao()} | "
                f"Status: {self.get_status()} | "
                f"CPF: {self.get_cpf()}")
