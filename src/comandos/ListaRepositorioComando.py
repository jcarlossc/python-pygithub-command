class ListaRepositorioComando(ChildProcessError):
    def __init__(self, servico):
        self.servico = servico

    def executar(self):
        repositorios = self.servico.listar_repositorios()
        if repositorios:
            print("REPOSITÓRIOS:")
            for i, repositorio in enumerate(repositorios, start = 1):
                print(f"{i}. {repositorio}")
