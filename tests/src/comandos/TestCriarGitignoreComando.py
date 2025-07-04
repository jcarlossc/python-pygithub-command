import unittest
from unittest.mock import MagicMock, patch
from src.comandos.CriarGitignoreComando import CriarGitignoreComando

class TestCriarGitignoreComando(unittest.TestCase):
    def test_executar_corretos(self):
        mock_servico = MagicMock()
        mock_servico.criar_arquivo.return_value = True

        comando = CriarGitignoreComando(
            servico = mock_servico,
            nome_repositorio = "repositório-exemplo"
        )

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.criar_arquivo.assert_called_once_with(
            "repositório-exemplo", ".gitignore", "*.pyc\n__pycache__/", "Add .gitignore"
        )
        mock_print.assert_called_once_with(".gitignore criado com sucesso.")

    def test_executar_falhar(self):
        mock_servico = MagicMock()
        mock_servico.criar_arquivo.return_value = False

        comando = CriarGitignoreComando(
            servico = mock_servico,
            nome_repositorio = "repositório-exemplo"
        )

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
