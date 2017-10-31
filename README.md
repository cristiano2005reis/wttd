# Eventex

Sistema de eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com python 3.6.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env.
6. Execute os testes.

```console
git clone git@github.com:cristiano2005reis/wttd.git wttd
cd wttd
python -m venv.wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#configuro o email
git push heroku master --force
```
