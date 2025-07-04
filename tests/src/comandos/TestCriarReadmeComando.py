# tests/src/comandos/test_criar_readme_comando.py

import unittest
from unittest.mock import MagicMock, patch
from src.comandos.CriarReadmeComando import CriarReadmeComando

class TestCriarReadmeComando(unittest.TestCase):
    def test_executar_corretos(self):
        mock_servico = MagicMock()
        mock_servico.criar_arquivo.return_value = True

        comando = CriarReadmeComando(
            servico=mock_servico,
            nome_repositorio="repositório-teste"
        )

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_servico.criar_arquivo.assert_called_once_with(
            "repositório-teste", "README.md", "# Projeto pyGithub", "Add README"
        )
        mock_print.assert_called_once_with("README .md criado com sucesso.")

    def test_executar_falha(self):
        mock_servico = MagicMock()
        mock_servico.criar_arquivo.return_value = False

        comando = CriarReadmeComando(
            servico=mock_servico,
            nome_repositorio="repositório-teste"
        )

        with patch("builtins.print") as mock_print:
            comando.executar()

        mock_print.assert_not_called()

if __name__ == "__main__":
    unittest.main()
