from src.comandos.Comando import Comando

class ListaRepositorioComando(Comando):
    """
    Classe que representa o comando para listar repositórios do usuário.
    """
    def __init__(self, servico):
        """
        Inicializa a classe que representa a listagem de repositórios.

        Atributos:
            serviço (Servico): Instância da classe ServiçoGithub.
        """
        self.servico = servico

    def executar(self):
        """
        Executa a listagem de repositórios.
        """
        repositorios = self.servico.listar_repositorios()
        if repositorios:
            print("REPOSITÓRIOS:")
            for i, repositorio in enumerate(repositorios, start = 1):
                print(f"{i}. {repositorio}")
