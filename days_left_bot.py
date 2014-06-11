# -*- coding: utf-8 -*-
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

    def get_tweet_msg(self, today):
        first_day = today.replace(month=1, day=1)
        last_day = today.replace(month=12, day=31)
        total_days = (last_day - first_day).days + 1
        past_days = (today - first_day).days
        return u'今年も {0}/{1} 日経過。あと {2} 日'.format(
            past_days, total_days, total_days - past_days)

    def tweet_current_datetime(self):
        JST = datetime.timedelta(hours=9)
        today = (datetime.datetime.utcnow() + JST).date()
        msg = self.get_tweet_msg(today)
        self.api.update_status(msg)
        return msg
