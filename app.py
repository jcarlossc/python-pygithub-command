import os
from src.comandos.ListaRepositorioComando import ListaRepositorioComando
from src.comandos.CriarRepositorioComando import CriarRepositorioComando
from src.comandos.CriarReadmeComando import CriarReadmeComando
from src.comandos.CriarGitignoreComando import CriarGitignoreComando
from src.comandos.ExcluirRepositorioComando import ExcluirRepositorioComando
from src.servico.ServicoGithub import ServicoGithub
from src.invocar.InvocarGithub import InvocarGithub

if __name__ == "__main__":

    # Use variável de ambiente para segurança
    TOKEN = os.getenv("GITHUB_TOKEN") or "SEU TOKEN"

    servico = ServicoGithub(TOKEN)
    invocar = InvocarGithub()

    # Lista repositórios
    invocar.adicionar_comandos(ListaRepositorioComando(servico))

    nome_repositorio = "repositorio-teste"

    # Cria repositório
    # invocar.adicionar_comandos(CriarRepositorioComando(servico, nome_repositorio))

    # Cria README.md
    # invocar.adicionar_comandos(CriarReadmeComando(servico, nome_repositorio))
    
    # Cria .gitignore
    # invocar.adicionar_comandos(CriarGitignoreComando(servico, nome_repositorio))

    # CUIDADO!!! Exclui repositório
    # invocar.adicionar_comandos(ExcluirRepositorioComando(servico, nome_repositorio))

    invocar.executar_comandos()