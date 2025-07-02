from github import Github
from github.GithubException import GithubException

class ServicoGithub:
    def __init__(self, token):
        self.github = Github(token)
        self.usuario = self.github.get_user()

    def listar_repositorios(self):
        try:
            return [repositorio.name for repositorio in self.usuario.get_repos()]   

        except GithubException as e:
            print(f"Falha ao listar repositórios: {e}")
            return []
        
    def criar_repositorio(self, nome):
        try: 
            return self.usuario.create_repo(nome)  
        
        except GithubException as e:
            print(f"Falha ao criar repositório: {e}")
            return None

    def criar_arquivo(self, nome_repositorio, path, conteudo, mensagem="add file"):
        try:
            repositorio = self.github.get_repo(f"{self.usuario.login}/{nome_repositorio}")
            repositorio.create_file(path, mensagem, conteudo)
            return True
        
        except GithubException as e:
            print(f"Falha ao criar arquivo 'path' {e}")

    def excluir_repositorio(self, nome):
        try:
            repositorio = self.github.get_repo(f"{self.usuario.login}/{nome}")    
            repositorio.delete()
            return True
        
        except GithubException as e:
            print(f"Falha ao excluir repositório 'nome': {e}")

