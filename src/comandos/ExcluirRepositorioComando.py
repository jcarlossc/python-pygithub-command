from src.comandos.Comando import Comando

class ExcluirRepositorioComando(Comando):
    def __init__(self, servico, nome_repositorio):
        self.servico = servico
        self.nome_repositorio = nome_repositorio

    def executar(self):
        if self.servico.excluir_repositorio(self.nome_repositorio):
            print(f"Repositório {self.nome_repositorio} excluído com sucesso.")    