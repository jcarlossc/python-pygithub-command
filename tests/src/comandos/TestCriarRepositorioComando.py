import unittest
from unittest.mock import MagicMock, patch
from src.comandos.CriarRepositorioComando import CriarRepositorioComando

class TestCriarRepositorioComando(unittest.TestCase):
    def test_cria_repositorio_com_sucesso(self):
        mock_servico = MagicMock()
        mock_repositorio = MagicMock()
        mock_repositorio.html_url = "https://github.com/user/repositorio-teste"
        mock_servico.criar_repositorio.return_value = mock_repositorio

        comando = CriarRepositorioComando(mock_servico, "repositorio-teste")

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.criar_repositorio.assert_called_once_with("repositorio-teste")
        mock_print.assert_called_once_with("Repositório criado com sucesso: https://github.com/user/repositorio-teste")

    def test_cria_repositorio_com_falha(self):
        mock_servico = MagicMock()
        mock_servico.criar_repositorio.return_value = None

        comando = CriarRepositorioComando(mock_servico, "repositorio-teste")

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.criar_repositorio.assert_called_once_with("repositorio-teste")
        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
