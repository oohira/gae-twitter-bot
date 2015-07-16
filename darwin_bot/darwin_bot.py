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
    BASE_URL = 'http://www.nhk.or.jp/darwin/broadcasting/'
    ARCHIVE_URL = 'http://cgi2.nhk.or.jp/darwin/broadcasting/'

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

    def parse_program(self, html):
        soup = BeautifulSoup(html)
        div = soup.select('#mainConMain')[0]
        title = u'第' + div.h3.string
        date = unicodedata.normalize('NFKC', div.p.string)
        regexp = re.compile(u'[^\d]*((\d+)月(\d+)日\(日\)午後(\d+)時(\d+)分)')
        match = regexp.match(date)
        return {
            'title': title,
            'date': match.group(1),
            'month': int(match.group(2)),
            'day': int(match.group(3))
        }

    def get_next_program(self):
        html = urllib2.urlopen(self.BASE_URL + 'next.html')
        program = self.parse_program(html)
        month = program['month']
        day = program['day']
        now = datetime.datetime.now(self.JST)
        year = now.year if month >= now.month else now.year + 1
        return self.get_archived_program(year, month, day)

    def get_prev_program(self):
        html = urllib2.urlopen(self.BASE_URL + 'review.html')
        program = self.parse_program(html)
        month = program['month']
        day = program['day']
        now = datetime.datetime.now(self.JST)
        year = now.year if month <= now.month else now.year - 1
        return self.get_archived_program(year, month, day)

    def get_archived_program(self, year, month, day):
        url = self.ARCHIVE_URL + 'date.cgi?p={0}&q={1}'.format(year, month)
        html = urllib2.urlopen(url)
        soup = BeautifulSoup(html)
        for elem in soup.select('#resultArea .eachInfo > dl'):
            dd = elem.find_all('dd')
            if dd[0].string == '{0}/{1}/{2}'.format(year, month, day):
                return {
                    'url': self.ARCHIVE_URL + dd[1].a.get('href'),
                    'title': dd[1].string,
                    'date': u'{0}年{1}月{2}日'.format(year, month, day),
                    'animals': dd[2].string.split(u'・')
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
