from src.comandos.Comando import Comando

class CriarRepositorioComando(Comando):
    """
    Classe que representa o comando para criar um novo repositório.
    """
    def __init__(self, servico, nome_repositorio):
        """
        Inicializa a classe que representa a criação de um repositório.

        Atributos:
            serviço (Servico): Instância da classe ServiçoGithub.
            nome_repositório (str): Nome do repositório.
        """
        self.servico = servico
        self.nome_repositorio = nome_repositorio

    def executar(self):
        """
        Executa a criação do repositório.
        """
        repositorio = self.servico.criar_repositorio(self.nome_repositorio)
        if repositorio:
            print(f"Repositório criado com sucesso: {repositorio.html_url}")    