from src.comandos.Comando import Comando

class CriarReadmeComando(Comando):
    """
    Classe que representa o Comando para criar um arquivo README.md em um repositório.
    """
    def __init__(self, servico, nome_repositorio, conteudo="# Projeto pyGithub"):
        """
        Inicializa a classe que representa a criação de arquivo README.

        Atributos:
            serviço (Servico): Instância da classe ServiçoGithub.
            nome_repositório (str): Nome do repositório.
            conteúdo (str): Texto de exemplo para o arquivo README.
        """
        self.servico = servico
        self.nome_repositorio = nome_repositorio
        self.conteudo = conteudo

    def executar(self):
        """
        Cria o arquivo README.md no repositório especificado.
        """
        if self.servico.criar_arquivo(self.nome_repositorio, "README.md", self.conteudo, "Add README"):  
            print("README .md criado com sucesso.")      