# Automação de tarefas na Plataforma GitHub com PyGithub

Estudo sobre orientação a objetos em Python e uso do módulo **PyGithub** para automação de ações na plataforma GitHub. O projeto foi implementado com base no **padrão de projeto comportamental Command (Comando)**.

---

## Funcionalidades

- Listar repositórios
- Criar repositório
- Criar arquivo `README.md`
- Criar arquivo `.gitignore`
- Excluir repositório

---

## Como gerar o token no GitHub

1. Acesse [https://github.com](https://github.com) e faça login.
2. No canto superior direito, clique na foto do perfil e depois em **Settings**.
3. No menu lateral esquerdo, clique em **Developer settings** (último item).
4. Clique em **Personal access tokens** > **Tokens (classic)**.
5. Clique em **Generate new token** > **Generate new token (classic)**.
6. (Opcional) Dê um nome ao token.
7. Escolha a validade do token (Expiration).
8. Em **Select scopes**, marque as opções `repo` e `delete_repo`.
9. Clique em **Generate token**.
10. Copie e utilize esse token no seu código (arquivo principal `app.py` ou via variável de ambiente `GITHUB_TOKEN`).

---

## Ferramentas utilizadas

- Python 3.9.13
- Ambiente virtual `venv`
- Módulo `PyGithub`
- `unittest` para testes
- Git/GitHub
- Visual Studio Code
- Sistema operacional Windows 10

---

## Requisitos

- Python 3.x
- Módulo `PyGithub`
- Token do GitHub com permissões adequadas

---

## Como utilizar

```bash
# Clone o repositório
git clone https://github.com/jcarlossc/python-pygithub-command.git

# Acesse o diretório
cd python-pygithub-command

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py

# Para sair do ambiente virtual
deactivate
```
---

## Contribuição:

Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

---

## Licença:

Este projeto é licenciado sob a Licença MIT.

---

## Comandos importantes:

```bash
python -m venv venv               # Cria um ambiente virtual
venv\Scripts\activate             # Ativa o ambiente no Windows
source venv/bin/activate          # Ativa o ambiente no Linux/macOS
deactivate                        # Encerra o ambiente virtual

pip install nome-pacote           # Instala um pacote
pip uninstall nome-pacote         # Remove um pacote
pip freeze > requirements.txt     # Gera (ou atualiza) o arquivo de dependências
pip install -r requirements.txt   # Instala pacotes listados no requirements.txt
pip list                          # Lista pacotes instalados
pip show nome-pacote              # Exibe detalhes de um pacote
```
