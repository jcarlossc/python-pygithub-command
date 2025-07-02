from src.comandos.Comando import Comando

class CriarReadmeComando(Comando):
    def __init__(self, servico, nome_repositorio, conteudo="# Projeto pyGithub"):
        self.servico = servico
        self.nome_repositorio = nome_repositorio
        self.conteudo = conteudo

    def executar(self):
        if self.servico.criar_arquivo(self.nome_repositorio, "README.md", self.conteudo, "Add README"):  
            print('README .md criado com sucesso.')      