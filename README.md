# EVENTEX

Sistema de eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/gpedroso/eventex.svg?branch=master)](https://travis-ci.org/gpedroso/eventex)
[![Code Health](https://landscape.io/github/gpedroso/eventex/master/landscape.svg?style=flat)](https://landscape.io/github/gpedroso/eventex/master)

Textile

!https://landscape.io/github/gpedroso/eventex/master/landscape.svg?style=flat!:https://landscape.io/github/gpedroso/eventex/master

RST / Sphinx

.. image:: https://landscape.io/github/gpedroso/eventex/master/landscape.svg?style=flat
   :target: https://landscape.io/github/gpedroso/eventex/master
   :alt: Code Health

HTML

<a href="https://landscape.io/github/gpedroso/eventex/master">
  <img alt="Code Health" src="https://landscape.io/github/gpedroso/eventex/master/landscape.svg?style=flat"/>
</a>


## Como desenvolver

1. clone o repositório
2. Cria um virtualenv com python 3.5
3. Ative o virtualenv
4. Instale as dependências.
5. Configura a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:gpedroso/eventex.git wttd
cd wttd
python -m venv .wttd
.wttd/Scripts/activate.bat
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie a instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY para a instância.
4. Defina DEBUG=FALSE
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
```
