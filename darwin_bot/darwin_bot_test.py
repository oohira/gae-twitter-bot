# -*- coding: utf-8 -*-
import darwin_bot
import unittest


class DarwinBotTest(unittest.TestCase):
    def setUp(self):
        self.bot = darwin_bot.DarwinBot()

    def test_parse_program(self):
        html = u"""
        <html>
          <body>
            <div id="mainConMain">
              <h2>次回放送</h2>
              <h3>413回「祖鳥の生き残り！？　翼にツメを持つ鳥」</h3>
              <p class="onairTime">【総合・地上デジタル】５月３１日（日）午後７時３０分～</p>
            </div>
          </body>
        </html>
        """
        program = self.bot.parse_program(html)
        self.assertEqual(program['title'],
            u'第413回「祖鳥の生き残り！？　翼にツメを持つ鳥」')
        self.assertEqual(program['date'], u'5月31日(日)午後7時30分')

    # def test_get_next_program(self):
    #     program = self.bot.get_next_program()
    #     self.assertEqual(program['title'],
    #         u'第414回「狩る！守る！巨大ワニの素顔」')
    #     self.assertEqual(program['date'], u'2015年6月7日')
    #     self.assertEqual(program['url'],
    #         u'http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p414')
    #     self.assertEqual(program['animals'], [u'ナイルワニ'])

    # def test_get_prev_program(self):
    #     program = self.bot.get_prev_program()
    #     self.assertEqual(program['title'],
    #         u'第413回「祖鳥の生き残り！？　翼にツメを持つ鳥」')
    #     self.assertEqual(program['date'], u'2015年5月31日')
    #     self.assertEqual(program['url'],
    #         u'http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p413')
    #     self.assertEqual(program['animals'], [u'ツメバケイ'])

    def test_get_archived_program(self):
        program = self.bot.get_archived_program(2015, 3, 15)
        self.assertEqual(program['title'],
            u'第403回「スクープ特集　仰天！スゴ腕のハンターたち」')
        self.assertEqual(program['date'], u'2015年3月15日')
        self.assertEqual(program['url'],
            u'http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p403')
        self.assertEqual(program['animals'],
            [u'ハシビロコウ', u'ハナカマキリ', u'ハチクマ'])

        program = self.bot.get_archived_program(2006, 4, 9)
        self.assertEqual(program['title'],
            u'第001回「古代魚が跳んだ！」')
        self.assertEqual(program['date'], u'2006年4月9日')
        self.assertEqual(program['url'],
            u'http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p001')
        self.assertEqual(program['animals'], [u'アロワナ'])

        program = self.bot.get_archived_program(2006, 4, 1)
        self.assertEqual(program, None)

    def test_get_tweet_msg(self):
        self.assertEqual(self.bot.get_tweet_msg(2015, 3, 20, 19), None)
        self.assertEqual(self.bot.get_tweet_msg(2015, 3, 21, 18), None)
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 3, 21, 19),
            u'明日の放送は、第404回「スクープ特集　一致団結！助け合う生きものたち」 2015年3月22日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p404 #ダーウィンが来た #ワオキツネザル #ハキリアリ #リカオン')
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 3, 22, 19),
            u'まもなく放送！第404回「スクープ特集　一致団結！助け合う生きものたち」 2015年3月22日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p404 #ダーウィンが来た #ワオキツネザル #ハキリアリ #リカオン')
        self.assertEqual(
            self.bot.get_tweet_msg(2015, 3, 22, 20),
            u'次回の放送は、第405回「荒野の育メン鳥　恋に子育てに全力疾走！」 2015年3月29日(日)午後7時30分〜 http://cgi2.nhk.or.jp/darwin/broadcasting/detail.cgi?p=p405 #ダーウィンが来た #ダーウィンレア')
