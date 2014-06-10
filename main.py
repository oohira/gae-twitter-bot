import days_left_bot
import webapp2
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))


class DaysLeftBotHandler(webapp2.RequestHandler):
    def get(self):
        bot = days_left_bot.DaysLeftBot()
        msg = bot.tweet_current_datetime()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(msg)


application = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/days-left-bot', DaysLeftBotHandler),
], debug=True)
