# AutoPrime — site de vendas de carros (Django)

## Como rodar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations carros
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin (cadastre os carros e leia os contatos): http://127.0.0.1:8000/admin/

## Estrutura

```
autoprime_projeto/
├── manage.py
├── requirements.txt
├── autoprime/            # projeto principal (settings, urls, wsgi/asgi)
├── carros/               # app: models, views, forms, urls, admin e templates
│   └── templates/carros/
│       ├── vendas_carros.html
│       └── detalhe_carro.html
├── static/img/           # hero-carro.jpg e sem-foto.jpg (placeholders)
└── media/                # fotos enviadas pelo admin (criada automaticamente)
```

## Variáveis de ambiente (produção)

| Variável | Exemplo |
|---|---|
| `DJANGO_SECRET_KEY` | uma chave longa e aleatória |
| `DJANGO_DEBUG` | `0` |
| `DJANGO_ALLOWED_HOSTS` | `meusite.com.br,www.meusite.com.br` |
