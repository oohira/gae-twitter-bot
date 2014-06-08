import datetime
import tweepy
import webapp2
import yaml
from google.appengine.api import users


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))


class DaysLeftBot(webapp2.RequestHandler):
    def get(self):
        msg = self.tweet_current_datetime()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(msg)

    def tweet_current_datetime(self):
        config = yaml.safe_load(open('config.yaml').read())
        auth = tweepy.OAuthHandler(config['API_KEY'], config['API_SECRET'])
        auth.set_access_token(
            config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])
        api = tweepy.API(auth)
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        msg = 'Now {0:%Y-%m-%d %H:%M:%S} JST'.format(now)
        api.update_status(msg)
        return msg


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/days-left-bot', DaysLeftBot),
], debug=True)
