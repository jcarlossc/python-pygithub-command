import unittest
from unittest.mock import patch, MagicMock
from src.servico.ServicoGithub import ServicoGithub

class TestServicoGithub(unittest.TestCase):

    @patch("src.servico.ServicoGithub.Github")
    def setUp(self, mock_github_classe):
        # Mock do Github.
        self.mock_github = MagicMock()
        # Mock do usuário.
        self.mock_usuario = MagicMock()

        mock_github_classe.return_value = self.mock_github
        self.mock_github.get_user.return_value = self.mock_usuario

        # Instância do serviço com token falso.
        self.servico = ServicoGithub("token_falso")

    def test_listar_repositorios_sucesso(self):
        # Simula dois repositórios.
        repositorio1 = MagicMock(name="repositorio1")
        repositorio2 = MagicMock(name="repositorio2")
        repositorio1.name = "repositorio1"
        repositorio2.name = "repositorio2"

        self.mock_usuario.get_repos.return_value = [repositorio1, repositorio2]

        resultado = self.servico.listar_repositorios()
        self.assertEqual(resultado, ["repositorio1", "repositorio2"])

    def test_listar_repositorios_falha(self):
        from github.GithubException import GithubException
        self.mock_usuario.get_repos.side_effect = GithubException(500, "Erro", None)

        resultado = self.servico.listar_repositorios()
        self.assertEqual(resultado, [])

    def test_criar_repositorio_sucesso(self):
        mock_repositorio = MagicMock()
        self.mock_usuario.create_repo.return_value = mock_repositorio

        resultado = self.servico.criar_repositorio("meu-repositório")
        self.assertEqual(resultado, mock_repositorio)
        self.mock_usuario.create_repo.assert_called_with("meu-repositório")

    def test_criar_repositorio_falha(self):
        from github.GithubException import GithubException
        self.mock_usuario.create_repo.side_effect = GithubException(400, "Erro", None)

        resultado = self.servico.criar_repositorio("erro-repo")
        self.assertIsNone(resultado)

    def test_criar_arquivo_sucesso(self):
        mock_repositorio = MagicMock()
        self.mock_github.get_repo.return_value = mock_repositorio

        sucesso = self.servico.criar_arquivo("repo", "file.txt", "conteúdo")
        self.assertTrue(sucesso)
        mock_repositorio.create_file.assert_called_with("file.txt", "add file", "conteúdo")

    def test_criar_arquivo_falha(self):
        from github.GithubException import GithubException
        self.mock_github.get_repo.side_effect = GithubException(404, "Não encontrado", None)

        sucesso = self.servico.criar_arquivo("repo", "file.txt", "conteúdo")
        self.assertIsNone(sucesso)  # Porque o método não tem return False explicito.

    def test_excluir_repositorio_sucesso(self):
        mock_repositorio = MagicMock()
        self.mock_github.get_repo.return_value = mock_repositorio

        sucesso = self.servico.excluir_repositorio("repo-apagar")
        self.assertTrue(sucesso)
        mock_repositorio.delete.assert_called_once()

    def test_excluir_repositorio_falha(self):
        from github.GithubException import GithubException
        self.mock_github.get_repo.side_effect = GithubException(404, "Não encontrado", None)

        sucesso = self.servico.excluir_repositorio("repo-inexistente")
        self.assertFalse(sucesso)

if __name__ == '__main__':
    unittest.main()
