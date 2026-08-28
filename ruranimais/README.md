# Ruranimais

Projeto acadêmico em Python/Flask para registrar e acompanhar cães e gatos encontrados no campus da UFRPE.

## Requisitos e instalação

Instale Python 3.10 ou superior. No terminal do VS Code, na pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Execução

```powershell
python app.py
```

Abra http://127.0.0.1:5000. O arquivo `database.db` e as tabelas `usuarios` e `animais` são criados automaticamente.

## Teste

Use **Criar conta** com um e-mail como `estudante@ufrpe.br`. Um endereço como `estudante@gmail.com` deve ser rejeitado no backend. Depois faça login, acesse **Cadastrar animal**, preencha espécie e localização e salve. O registro aparecerá no Dashboard com ID único. Ao clicar em **Sair**, o acesso direto a `/dashboard` deve redirecionar para o login.

## Arquivos

`app.py` contém o Flask, as rotas, as sessões, as validações, o hash das senhas e todo o código SQLite. Os cinco arquivos HTML ficam na raiz e são renderizados pelo Flask com `template_folder="."`; `style.css` e `script.js` também ficam na raiz e são servidos por `static_folder="."`. `requirements.txt` lista Flask. `database.db` é o banco local criado em tempo de execução.

Mapa real, geolocalização, e-mail, imagens e permissões complexas ficam para versões futuras.
