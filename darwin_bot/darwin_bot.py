# -*- coding: utf-8 -*-
import datetime
import os
import pytz
import re
import tweepy
import unicodedata
import urllib2
import yaml
from bs4 import BeautifulSoup


class DarwinBot:
    JST = pytz.timezone('Asia/Tokyo')
    BASE_URL = 'http://cgi2.nhk.or.jp/darwin/articles/'
    ARCHIVE_URL = 'http://cgi2.nhk.or.jp/darwin/articles/'

    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'config.yaml')
        config = yaml.safe_load(open(path).read())
        auth = tweepy.OAuthHandler(config['API_KEY'], config['API_SECRET'])
        auth.set_access_token(
            config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(auth)

    def first_sunday_on_or_after(self, dt):
        days_to_go = 6 - dt.weekday()
        if days_to_go:
            dt += datetime.timedelta(days_to_go)
        return dt

    def get_archived_program(self, year, month, day):
        url = self.ARCHIVE_URL + 'date.cgi?p={0}&q={1}'.format(year, month)
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)
        for elem in soup.select('#articleList > li'):
            date = elem.find('p', class_='articleDate').string.lstrip(u'[放送日]')
            if date == '{0}/{1}/{2}'.format(year, month, day):
                title = elem.find('p', class_='articleTitle')
                animals = elem.find('p', class_='articleName').string.lstrip(u'[登場動物]')
                return {
                    'url': self.ARCHIVE_URL + title.a.get('href'),
                    'title': title.string.strip(),
                    'date': u'{0}年{1}月{2}日'.format(year, month, day),
                    'animals': animals.split(u'・')
                }

    def tweet_current_datetime(self):
        now = datetime.datetime.now(self.JST)
        msg = self.get_tweet_msg(now.year, now.month, now.day, now.hour)
        if msg:
            self.api.update_status(msg)
        return msg

    def get_tweet_msg(self, year, month, day, hour):
        today = datetime.datetime(year, month, day, hour, tzinfo=self.JST)
        sun = self.first_sunday_on_or_after(today)
        remaining_days = (sun - today).days
        if remaining_days == 0 and hour == 20:
            sun += datetime.timedelta(days=7)
            program = self.get_archived_program(sun.year, sun.month, sun.day)
            if program:
                return u'次回の放送は、' + self.get_program_msg(program)
        else:
            program = self.get_archived_program(sun.year, sun.month, sun.day)
            if not program:
                return
            if remaining_days == 0 and hour == 19:
                return u'まもなく放送！' + self.get_program_msg(program)
            elif remaining_days == 1 and hour == 19:
                return u'明日の放送は、' + self.get_program_msg(program)

    def get_program_msg(self, program):
        msg = u'{0} {1}(日)午後7時30分〜 {2} #ダーウィンが来た'.format(
            program['title'], program['date'], program['url'])
        for animal in program['animals'][:3]:
            msg += u' #' + animal
        return msg
