import unittest
from unittest.mock import Mock
from src.invocar.InvocarGithub import InvocarGithub

class TestInvocarGithub(unittest.TestCase):
    def test_adicionar_comandos(self):
        invocador = InvocarGithub()
        comando_mock = Mock()

        invocador.adicionar_comandos(comando_mock)

        self.assertIn(comando_mock, invocador.comandos)
        self.assertEqual(len(invocador.comandos), 1)

    def test_executar_comandos_chama_executar(self):
        invocador = InvocarGithub()

        comando1 = Mock()
        comando2 = Mock()

        invocador.adicionar_comandos(comando1)
        invocador.adicionar_comandos(comando2)

        invocador.executar_comandos()

        comando1.executar.assert_called_once()
        comando2.executar.assert_called_once()

if __name__ == "__main__":
    unittest.main()
