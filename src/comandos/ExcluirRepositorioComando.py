from src.comandos.Comando import Comando

class ExcluirRepositorioComando(Comando):
    """
    Classe que representa o comando para excluir um repositório.
    """
    def __init__(self, servico, nome_repositorio):
        """
        Inicializa a classe que representa a exclusão de um repositório.

        Atributos:
            serviço (Servico): Instância da classe ServiçoGithub.
            nome_repositório (str): Nome do repositório.
        """
        self.servico = servico
        self.nome_repositorio = nome_repositorio

    def executar(self):
        """
        Executa a exclusão do repositório.
        """
        if self.servico.excluir_repositorio(self.nome_repositorio):
            print(f"Repositório {self.nome_repositorio} excluído com sucesso.")    