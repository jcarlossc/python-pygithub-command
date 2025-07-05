import unittest
from unittest.mock import MagicMock, patch
from src.comandos.ListaRepositorioComando import ListaRepositorioComando

class TestListaRepositorioComando(unittest.TestCase):
    def test_lista_repositorios_sucesso(self):
        mock_servico = MagicMock()
        mock_servico.listar_repositorios.return_value = ["repositorio1", "repositorio2", "repositorio3"]
        comando = ListaRepositorioComando(mock_servico)

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.listar_repositorios.assert_called_once()
        mock_print.assert_any_call("REPOSITÓRIOS:")
        mock_print.assert_any_call("1. repositorio1")
        mock_print.assert_any_call("2. repositorio2")
        mock_print.assert_any_call("3. repositorio3")

    def test_lista_repositorios_falha(self):
        mock_servico = MagicMock()
        mock_servico.listar_repositorios.return_value = []
        comando = ListaRepositorioComando(mock_servico)

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.listar_repositorios.assert_called_once()
        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
