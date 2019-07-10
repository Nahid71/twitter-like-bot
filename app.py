from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# define the bot class


class TwitterBot:
    def __init__(self, username, password):
        # setting the email and password
        self.username = username
        self.password = password
        # init the firefox driver
        self.bot = webdriver.Firefox()
    # define login method to ligin in twitter account

    def login(self):
        bot = self.bot
        # set the url
        bot.get('https://twitter.com/')
        # set sleeping time to load the full page
        time.sleep(3)
        # select the email and password fields
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        # first clear those fields
        email.clear()
        password.clear()
        # filup the email and password fields
        email.send_keys(self.username)
        password.send_keys(self.password)
        # click ENTER key to login
        password.send_keys(Keys.RETURN)
        # set sleeping time to load the full page
        time.sleep(3)
    # define lilke method to like the tweet

    def like(self, hashtag):
        bot = self.bot
        # get the search url
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typd')
        # set sleeping time to load the full page
        time.sleep(3)
        # scroll the search page
        for i in range(1, 5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            # grabs all the tweets and their link
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            for link in links:
              # goto the tweet
                bot.get('https://twitter.com' + link)
                try:
                  # click in like botton
                    bot.find_element_by_class_name('HeartAnimation').click()
                    # and sleep for 10 seconds
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


# init the TwitterBot object
nahid = TwitterBot('nahid8698@yahoo.com', '******')
# call the login method to login
nahid.login()
# call the like method to like all the tweets
nahid.like('web development')
