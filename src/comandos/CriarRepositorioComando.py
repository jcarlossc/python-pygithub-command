from src.comandos.Comando import Comando

class CriarRepositorioComando(Comando):
    def __init__(self, servico, nome_repositorio):
        self.servico = servico
        self.nome_repositorio = nome_repositorio

    def executar(self):
        repositorio = self.servico.criar_repositorio(self.nome_repositorio)
        if repositorio:
            print(f"Repositório criado com sucesso: {repositorio.html_url}")    