import time

from speedteest import Internetservicetweetbot

bot = Internetservicetweetbot()
bot.get_internet_speed()
time.sleep(5)
bot.tweet_at_provider()
