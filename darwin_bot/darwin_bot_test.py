# -*- coding: utf-8 -*-
import darwin_bot
import unittest


class DarwinBotTest(unittest.TestCase):
    def setUp(self):
        self.bot = darwin_bot.DarwinBot()

    def test_get_archived_program(self):
        program = self.bot.get_archived_program(2015, 3, 15)
        self.assertEqual(program['title'],
            u'第403回「スクープ特集　仰天！スゴ腕のハンターたち」')
        self.assertEqual(program['date'], u'2015年3月15日')
        self.assertEqual(program['url'],
            u'http://cgi2.nhk.or.jp/darwin/articles/detail.cgi?p=p403')
        self.assertEqual(program['animals'],
            [u'ハシビロコウ', u'ハナカマキリ', u'ハチクマ'])

        program = self.bot.get_archived_program(2006, 4, 9)
        self.assertEqual(program['title'],
            u'第001回「古代魚が跳んだ！」')
        self.assertEqual(program['date'], u'2006年4月9日')
        self.assertEqual(program['url'],
            u'http://cgi2.nhk.or.jp/darwin/articles/detail.cgi?p=p001')
        self.assertEqual(program['animals'], [u'アロワナ'])

        program = self.bot.get_archived_program(2006, 4, 1)
        self.assertEqual(program, None)

    def test_get_tweet_msg(self):
        self.assertEqual(self.bot.get_tweet_msg(2015, 3, 20, 19), None)
        self.assertEqual(self.bot.get_tweet_msg(2015, 3, 21, 18), None)
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 3, 21, 19),
            u'明日の放送は、第404回「スクープ特集　一致団結！助け合う生きものたち」 2015年3月22日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/articles/detail.cgi?p=p404 #ダーウィンが来た #ワオキツネザル #ハキリアリ #リカオン')
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 3, 22, 19),
            u'まもなく放送！第404回「スクープ特集　一致団結！助け合う生きものたち」 2015年3月22日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/articles/detail.cgi?p=p404 #ダーウィンが来た #ワオキツネザル #ハキリアリ #リカオン')
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 3, 22, 20),
            u'次回の放送は、第405回「荒野の育メン鳥　恋に子育てに全力疾走！」 2015年3月29日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/articles/detail.cgi?p=p405 #ダーウィンが来た #ダーウィンレア')

    def test_get_too_long_tweet_msg(self):
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 7, 12, 20),
            u'次回の放送は、第420回「発見！海水浴場の大自然」 2015年7月19日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/articles/detail.cgi?p=p420 #ダーウィンが来た #イシダイ #ミジンベニハゼ #タコ')
