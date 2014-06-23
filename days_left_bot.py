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

    def tweet_current_datetime(self):
        JST = datetime.timedelta(hours=9)
        now = datetime.datetime.utcnow() + JST
        msg = self.get_tweet_msg(now.year, now.month, now.day, now.hour)
        if msg:
            self.api.update_status(msg + u' #あと何日')
        return msg

    def get_tweet_msg(self, year, month, day, hour):
        today = datetime.date(year, month, day)
        first_day = datetime.date(year, 1, 1)
        last_day = datetime.date(year, 12, 31)
        if hour == 0:
            return self.get_daily_tweet_msg(today, first_day, last_day)
        elif today.day == 1 and hour == 12:
            return self.get_monthly_tweet_msg(today)
        else:
            return ''

    def get_daily_tweet_msg(self, today, first_day, last_day):
        total_days = (last_day - first_day).days + 1
        past_days = (today - first_day).days
        past_percentage = 100.0 * past_days / total_days
        if past_days == 0:
            return u'{0} 年あけましておめでとうございます。今年はあと {1} 日' \
                .format(today.year, total_days)
        elif past_days == total_days - 1:
            return u'{0} 年もいよいよ大晦日。今年もあと 1 日'.format(today.year)
        else:
            return u'今年も {0}/{1} 日経過 ({2:.1f}%)。あと {3} 日'.format(
                past_days, total_days, past_percentage, total_days - past_days)

    def get_monthly_tweet_msg(self, today):
        msg = u'{0} 年もあと {1} ヶ月'
        if today.month == 1:
            msg = u'{0} 年はどんなことに挑戦しますか？'
        elif today.month == 2:
            msg = u'{0} 年も 1 ヶ月が経ちました。一度振り返ってみては？'
        elif today.month == 7:
            msg = u'{0} 年もあと 6 ヶ月。今年の折り返し地点です'
        elif today.month == 12:
            msg = u'{0} 年もいよいよあと 1 ヶ月。ラストスパート！'
        else:
            msg = u'{0} 年もあと {1} ヶ月'
        return msg.format(today.year, 12 - today.month + 1)
