from github import Github
from github.GithubException import GithubException

class ServicoGithub:
    """
    Classe responsável por interagir com a API do GitHub.
    Atua como o 'Receiver' no padrão de projeto Command.
    """
    def __init__(self, token):
        """
        Inicializa o serviço Github com um token de autenticação.
        Cria usuário para o serviço.

        Atributos:
            token (str): Token de autenticação pessoal (PAT) do GitHub.
            github (Github): Instância autenticada da API do GitHub.
            usuario (AuthenticatedUser): Usuário autenticado obtido pela API.
        """
        self.github = Github(token)
        self.usuario = self.github.get_user()

    def listar_repositorios(self):
        """
        Lista os repositórios do usuário autenticado.

        Retorna: 
            Lista de nomes dos repositórios.

        Erro:
            GithubException: em caso de falha na comunicação com a API do GitHub.
        """
        try:
            return [repositorio.name for repositorio in self.usuario.get_repos()]   

        except GithubException as e:
            print(f"Falha ao listar repositórios: {e}")
            return []
        
    def criar_repositorio(self, nome):
        """
        Cria um novo repositório com o nome passado como parâmetro.

        Parâmetro: 
            nome (str): Nome do novo repositório.

        Retorna: 
            Objeto do repositório criado.

        Erro:
            GithubException: em caso de falha na comunicação com a API do GitHub.
        """
        try: 
            return self.usuario.create_repo(nome)  
        
        except GithubException as e:
            print(f"Falha ao criar repositório: {e}")
            return None

    def criar_arquivo(self, nome_repositorio, path, conteudo, mensagem="add file"):
        """
        Cria um arquivo em um repositório.

        Parâmetros:
            nome_repositório (str): Nome do repositório.
            path (str): Caminho do arquivo.
            conteúdo (str): Conteúdo do arquivo.
            mensagem (str): Mensagem do commit.

        Retorna: 
            True se criado com sucesso, False em caso de erro.

        Erro:
            GithubException: em caso de falha na comunicação com a API do GitHub.
        """
        try:
            repositorio = self.github.get_repo(f"{self.usuario.login}/{nome_repositorio}")
            repositorio.create_file(path, mensagem, conteudo)
            return True
        
        except GithubException as e:
            print(f"Falha ao criar arquivo 'path' {e}")

    def excluir_repositorio(self, nome):
        """
        Exclui um repositório existente.

        Parâmetro:
            nome (str): Nome do repositório a ser excluído.

        Retorna:
            True se excluído com sucesso, False caso contrário.

        Erro:
            GithubException: em caso de falha na comunicação com a API do GitHub.    
        """
        try:
            repositorio = self.github.get_repo(f"{self.usuario.login}/{nome}")    
            repositorio.delete()
            return True
        
        except GithubException as e:
            print(f"Falha ao excluir repositório 'nome': {e}")

