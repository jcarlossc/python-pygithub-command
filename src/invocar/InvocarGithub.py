class InvocarGithub:
    """
    Invocador do padrão Command.
    Armazena e executa uma fila de comandos.
    """
    def __init__(self):
        self.comandos = []

    def adicionar_comandos(self, comando):
        """
        Adiciona um comando à fila.

        Parâmetro:
            comando (Comando): Instância de uma subclasse de Command.
        """
        self.comandos.append(comando)

    def executar_comandos(self):
        """
        Executa todos os comandos adicionados na ordem.
        """
        for comando in self.comandos:
            comando.executar()        