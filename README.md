This is a simple Django webapp for parsing webpages built for educational purposes


![image link](https://github.com/thefivekey/parse/raw/master/screenshot.png)

#### This app uses:

Django + Channels, Postgres, Celery w/ Redis backend

#### Installation:
If you have docker toolbox installed:

`$ git clone https://github.com/thefivekey/parse.git`

`$ docker-compose build`

`$ docker-compose up -d`

or (don't forget to change settings.py)

`$ pip install -r requirements.txt`

`$ python3.4 manage.py runserver:8000`

`$ celery -A parse worker -l info`

`$ redis-server`
