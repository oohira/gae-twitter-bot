# gae-twitter-bot

Some Twitter bots written in Python on Google App Engine.

## Debug

```
$ cd gae-twitter-bot/
$ vagrant up
$ vagrant ssh
[vagrant@localhost ~]$ cd /vagrant/
[vagrant@localhost vagrant]$ pip install -r requirements.txt -t lib
[vagrant@localhost vagrant]$ dev_appserver.py .
```

## Unit Test

```
[vagrant@localhost vagrant]$ python run_tests.py ~/google_appengine
```

## Deploy

```
[vagrant@localhost vagrant]$ vi app.yaml
application: your-app-id

[vagrant@localhost vagrant]$ vi days_left_bot/config.yaml
API_KEY: '<your_api_key>'
API_SECRET: '<your_api_secret>'
ACCESS_TOKEN: '<your_access_token>'
ACCESS_TOKEN_SECRET: '<your_access_token_secret>'

[vagrant@localhost vagrant]$ vi darwin_bot/config.yaml
API_KEY: '<your_api_key>'
API_SECRET: '<your_api_secret>'
ACCESS_TOKEN: '<your_access_token>'
ACCESS_TOKEN_SECRET: '<your_access_token_secret>'

[vagrant@localhost vagrant]$ appcfg.py -A <your-app-id> update .
```