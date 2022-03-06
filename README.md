# Gerenciador-de-Senhas

Este é um projeto de um gerenciador de senhas, feito utilizando o Python e suas bibliotecas Tkinter, random, json e pyperclip.

## Ambiente Virtual

Recomendo a utilização de um ambiente virtual para instalar as dependências do projeto de forma local

```bash
python -m venv .venv
cd .\.venv\Scripts\
.\activate.ps1
```

## Instalação

Use o [pip](https://pip.pypa.io/en/stable/) para instalar as dependências do projeto

```bash
pip install requirements.txt
```

## Utilização

```bash
python main.py
```

Ao iniciar o projeto, o usuário tera acesso a uma interface gráfica, onde poderá registrar credenciais de websites, checar credenciais de contas já cadastradas e gerar senhas aleatórias (de 12 a 18 caractéres, dentre números, símbolos e letras)

As senhas são salvas num arquivo data.json no diretório principal do projeto. Este arquivo é criado pelo programa caso seja a primeira utilização, e será consultado posteriormente.
