# -*- coding: utf-8 -*-
import datetime
import days_left_bot
import unittest


class DaysLeftBotTest(unittest.TestCase):
    def setUp(self):
        self.bot = days_left_bot.DaysLeftBot()

    def test_get_tweet_msg_normal_year(self):
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 1, 1)),
            u'2014 年あけましておめでとうございます。今年はあと 365 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 1, 2)),
            u'今年も 1/365 日経過 (0.3%)。あと 364 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 2, 1)),
            u'今年も 31/365 日経過 (8.5%)。あと 334 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 2, 28)),
            u'今年も 58/365 日経過 (15.9%)。あと 307 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 3, 1)),
            u'今年も 59/365 日経過 (16.2%)。あと 306 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 12, 30)),
            u'今年も 363/365 日経過 (99.5%)。あと 2 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2014, 12, 31)),
            u'2014 年もいよいよ大晦日。今年もあと 1 日')

    def test_get_tweet_msg_leap_year(self):
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 1, 1)),
            u'2012 年あけましておめでとうございます。今年はあと 366 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 1, 2)),
            u'今年も 1/366 日経過 (0.3%)。あと 365 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 2, 1)),
            u'今年も 31/366 日経過 (8.5%)。あと 335 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 2, 28)),
            u'今年も 58/366 日経過 (15.8%)。あと 308 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 2, 29)),
            u'今年も 59/366 日経過 (16.1%)。あと 307 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 3, 1)),
            u'今年も 60/366 日経過 (16.4%)。あと 306 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 12, 30)),
            u'今年も 364/366 日経過 (99.5%)。あと 2 日')
        self.assertEqual(
            self.bot.get_tweet_msg(datetime.date(2012, 12, 31)),
            u'2012 年もいよいよ大晦日。今年もあと 1 日')
