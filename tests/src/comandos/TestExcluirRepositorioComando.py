import unittest
from unittest.mock import MagicMock, patch
from src.comandos.ExcluirRepositorioComando import ExcluirRepositorioComando

class TestExcluirRepositorioComando(unittest.TestCase):
    def test_executar_exclui_repositorio_com_sucesso(self):
        mock_servico = MagicMock()
        mock_servico.excluir_repositorio.return_value = True

        comando = ExcluirRepositorioComando(mock_servico, "repositorio-teste")

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.excluir_repositorio.assert_called_once_with("repositorio-teste")
        mock_print.assert_called_once_with("Repositório repositorio-teste excluído com sucesso.")

    def test_executar_nao_imprime_quando_falha_na_exclusao(self):
        mock_servico = MagicMock()
        mock_servico.excluir_repositorio.return_value = False

        comando = ExcluirRepositorioComando(mock_servico, "repositorio-teste")

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.excluir_repositorio.assert_called_once_with("repositorio-teste")
        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
