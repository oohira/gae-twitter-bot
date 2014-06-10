import datetime
import tweepy
import yaml


class DaysLeftBot:
    def __init__(self):
        config = yaml.safe_load(open('config.yaml').read())
        auth = tweepy.OAuthHandler(config['API_KEY'], config['API_SECRET'])
        auth.set_access_token(
            config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth)

    def tweet_current_datetime(self):
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        msg = 'Now {0:%Y-%m-%d %H:%M:%S} JST'.format(now)
        self.api.update_status(msg)
        return msg
