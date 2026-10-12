import os
import re
import sqlite3
from functools import wraps
from html import escape
from pathlib import Path

from flask import Flask, flash, g, get_flashed_messages, redirect, request, send_file, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "database.db"

app = Flask(__name__, template_folder=".", static_folder=None)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "ruranimais-chave-desenvolvimento")

EMAIL_PATTERN = re.compile(r"^[^\s@]+@ufrpe\.br$", re.IGNORECASE)


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    connection = get_connection()
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha_hash TEXT NOT NULL,
            data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS animais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            especie TEXT NOT NULL CHECK (especie IN ('Cao', 'Gato')),
            sexo TEXT,
            cor TEXT,
            descricao TEXT,
            localizacao TEXT NOT NULL,
            status TEXT,
            observacoes TEXT,
            usuario_id INTEGER NOT NULL,
            data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
        );
        """
    )
    connection.commit()
    connection.close()


def render_html(filename, replacements=None):
    page = (BASE_DIR / filename).read_text(encoding="utf-8")
    messages = "".join(
        f'<div class="flash {escape(category)}" role="alert">{escape(message)}</div>'
        for category, message in get_flashed_messages(with_categories=True)
    )
    page = page.replace("__FLASH_MESSAGES__", messages)
    for key, value in (replacements or {}).items():
        page = page.replace(key, value)
    return page


@app.route("/style.css")
@app.route("/static/style.css")
def style():
    return send_file(BASE_DIR / "style.css", mimetype="text/css")


@app.route("/script.js")
@app.route("/static/script.js")
def script():
    return send_file(BASE_DIR / "script.js", mimetype="application/javascript")


@app.before_request
def load_logged_user():
    user_id = session.get("user_id")
    g.user = None
    if user_id is not None:
        connection = get_connection()
        g.user = connection.execute(
            "SELECT id, nome, email FROM usuarios WHERE id = ?", (user_id,)
        ).fetchone()
        connection.close()


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            flash("Você precisa estar logado para acessar esta página.", "error")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def index():
    return render_html("index.html")


@app.route("/cadastro", methods=("GET", "POST"))
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        confirmar_senha = request.form.get("confirmar_senha", "")
        error = None

        if not nome or not email or not senha or not confirmar_senha:
            error = "Preencha todos os campos obrigatórios."
        elif not EMAIL_PATTERN.fullmatch(email):
            error = "Utilize um e-mail institucional @ufrpe.br."
        elif senha != confirmar_senha:
            error = "As senhas não coincidem."
        elif len(senha) < 6:
            error = "A senha deve ter pelo menos 6 caracteres."

        if error is None:
            connection = get_connection()
            try:
                connection.execute(
                    "INSERT INTO usuarios (nome, email, senha_hash) VALUES (?, ?, ?)",
                    (nome, email, generate_password_hash(senha)),
                )
                connection.commit()
            except sqlite3.IntegrityError:
                error = "Este e-mail já possui uma conta."
            finally:
                connection.close()

        if error:
            flash(error, "error")
        else:
            flash("Cadastro realizado com sucesso. Agora você pode entrar.", "success")
            return redirect(url_for("login"))

    return render_html("cadastro.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        connection = get_connection()
        user = connection.execute(
            "SELECT * FROM usuarios WHERE email = ?", (email,)
        ).fetchone()
        connection.close()

        if user is None or not check_password_hash(user["senha_hash"], senha):
            flash("E-mail ou senha incorretos.", "error")
        else:
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["nome"]
            return redirect(url_for("dashboard"))

    return render_html("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "success")
    return redirect(url_for("index"))


@app.route("/dashboard")
@login_required
def dashboard():
    connection = get_connection()
    animals = connection.execute(
        """
        SELECT animais.*, usuarios.nome AS responsavel
        FROM animais JOIN usuarios ON usuarios.id = animais.usuario_id
        ORDER BY animais.data_cadastro DESC
        """
    ).fetchall()
    connection.close()
    cards = "".join(
        f'''<article class="animal-card"><div class="animal-icon">{'🐱' if animal['especie'] == 'Gato' else '🐶'}</div><div class="animal-info"><h3>{escape(animal['nome'] or 'Sem nome')}</h3><p>{'Cão' if animal['especie'] == 'Cao' else 'Gato'}{f" · {escape(animal['sexo'])}" if animal['sexo'] else ''}{f" · {escape(animal['cor'])}" if animal['cor'] else ''}</p><p class="muted">{escape(animal['localizacao'])}{f" · {escape(animal['status'])}" if animal['status'] else ''}</p></div><span class="record-id">#{animal['id']}</span></article>'''
        for animal in animals
    )
    empty = '<div class="empty-state"><span>🐾</span><h3>Ainda não há registros</h3><p>Comece o primeiro registro de um animal do campus.</p><a href="/animais/novo">Cadastrar um animal</a></div>'
    return render_html("dashboard.html", {"__USER_NAME__": escape(g.user["nome"].split()[0]), "__ANIMAL_CONTENT__": cards or empty, "__ANIMAL_COUNT__": str(len(animals))})


@app.route("/animais/novo", methods=("GET", "POST"))
@login_required
def cadastrar_animal():
    if request.method == "POST":
        fields = {
            "nome": request.form.get("nome", "").strip(),
            "especie": request.form.get("especie", "").strip(),
            "sexo": request.form.get("sexo", "").strip(),
            "cor": request.form.get("cor", "").strip(),
            "descricao": request.form.get("descricao", "").strip(),
            "localizacao": request.form.get("localizacao", "").strip(),
            "status": request.form.get("status", "").strip(),
            "observacoes": request.form.get("observacoes", "").strip(),
        }
        error = None
        if not fields["especie"] or not fields["localizacao"]:
            error = "Informe a espécie e o local onde o animal foi encontrado."
        elif fields["especie"] not in ("Cao", "Gato"):
            error = "Escolha cão ou gato como espécie."

        if error:
            flash(error, "error")
        else:
            connection = get_connection()
            connection.execute(
                """
                INSERT INTO animais
                (nome, especie, sexo, cor, descricao, localizacao, status, observacoes, usuario_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (*fields.values(), g.user["id"]),
            )
            connection.commit()
            connection.close()
            flash("Animal cadastrado com sucesso.", "success")
            return redirect(url_for("dashboard"))

    return render_html("cadastrar_animal.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
else:
    init_db()
