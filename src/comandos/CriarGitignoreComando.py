from src.comandos.Comando import Comando

class CriarGitignoreComando(Comando):
    """
    Classe que representa um Comando para criar um arquivo .gitignore em um repositório.
    """
    def __init__(self, servico, nome_repositorio, conteudo="*.pyc\n__pycache__/"):
        self.servico = servico
        self.nome_repositorio = nome_repositorio
        self.conteudo = conteudo

    def executar(self):
        """
        Cria o arquivo .gitignore no repositório especificado.
        """
        if self.servico.criar_arquivo(self.nome_repositorio, ".gitignore", self.conteudo, "Add .gitignore"):
            print(".gitignore criado com sucesso.")        