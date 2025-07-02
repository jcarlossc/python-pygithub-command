class InvocarGithub:
    def __init__(self):
        self.comandos = []

    def adicionar_comandos(self, comando):
        self.comandos.append(comando)

    def executar_comandos(self):
        for comando in self.comandos:
            comando.executar()        