# -*- coding: utf-8 -*-
import days_left_bot
import unittest


class DaysLeftBotTest(unittest.TestCase):
    def setUp(self):
        self.bot = days_left_bot.DaysLeftBot()

    def test_get_daily_tweet_msg_of_normal_year(self):
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 1, 1, 0),
            u'2014 年あけましておめでとうございます。今年はあと 365 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 1, 2, 0),
            u'今年も 1/365 日経過 (0.3%)。あと 364 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 2, 1, 0),
            u'今年も 31/365 日経過 (8.5%)。あと 334 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 2, 28, 0),
            u'今年も 58/365 日経過 (15.9%)。あと 307 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 3, 1, 0),
            u'今年も 59/365 日経過 (16.2%)。あと 306 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 12, 30, 0),
            u'今年も 363/365 日経過 (99.5%)。あと 2 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 12, 31, 0),
            u'2014 年もいよいよ大晦日。今年もあと 1 日')

    def test_get_daily_tweet_msg_of_leap_year(self):
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 1, 1, 0),
            u'2012 年あけましておめでとうございます。今年はあと 366 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 1, 2, 0),
            u'今年も 1/366 日経過 (0.3%)。あと 365 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 2, 1, 0),
            u'今年も 31/366 日経過 (8.5%)。あと 335 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 2, 28, 0),
            u'今年も 58/366 日経過 (15.8%)。あと 308 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 2, 29, 0),
            u'今年も 59/366 日経過 (16.1%)。あと 307 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 3, 1, 0),
            u'今年も 60/366 日経過 (16.4%)。あと 306 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 12, 30, 0),
            u'今年も 364/366 日経過 (99.5%)。あと 2 日')
        self.assertEqual(
            self.bot.get_tweet_msg(2012, 12, 31, 0),
            u'2012 年もいよいよ大晦日。今年もあと 1 日')

    def test_get_monthly_tweet_msg(self):
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 1, 1, 12),
            u'2014 年はどんなことに挑戦しますか？')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 2, 1, 12),
            u'2014 年も 1 ヶ月が経ちました。一度振り返ってみては？')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 3, 1, 12),
            u'2014 年もあと 10 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 4, 1, 12),
            u'2014 年もあと 9 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 5, 1, 12),
            u'2014 年もあと 8 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 6, 1, 12),
            u'2014 年もあと 7 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 7, 1, 12),
            u'2014 年もあと 6 ヶ月。今年の折り返し地点です')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 8, 1, 12),
            u'2014 年もあと 5 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 9, 1, 12),
            u'2014 年もあと 4 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 10, 1, 12),
            u'2014 年もあと 3 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 11, 1, 12),
            u'2014 年もあと 2 ヶ月')
        self.assertEqual(
            self.bot.get_tweet_msg(2014, 12, 1, 12),
            u'2014 年もいよいよあと 1 ヶ月。ラストスパート！')
