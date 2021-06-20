# Django Blog Tutorial

Neste guia vamos desenvolver um Blog completo com o framework Django e 
no final vamos fazer o deployment de nosso projeto na plataforma Heroku 
utilizando o sistema gerenciador de banco de dados PostgreSQL.

Leia o **[Tutorial](https://akiradev.netlify.app/posts/django-blog-heroku/)**

---

## Instalação

### Clone o Repositório

```
git clone https://github.com/the-akira/Django-Blog-Tutorial.git
```

### Dentro do Diretório Principal

Crie um Ambiente Virtual

```
python -m venv myvenv
```

Ative o Ambiente Virtual

```
source myvenv/bin/activate
```

Instale os Requeriments

```
pip install -r requirements.txt
```

Sincronize o banco de dados

```
python manage.py migrate
```

Execute a aplicação

```
python manage.py runserver
```

Navegue até `http://127.0.0.1:8000/` para ver a aplicação.
