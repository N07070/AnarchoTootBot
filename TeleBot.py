from TootBot import TootBot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, json, os, time

class TeleBot(object):
    """docstring for TeleBot."""
    def __init__(self, bot_token, channel_id, website_base_url, default_caption):
        super(TeleBot, self).__init__()
        self.bot_token = bot_token
        self.channel_id = channel_id
        self.website_base_url = website_base_url
        self.default_caption = default_caption
        self.visibility_of_last_toot = "public"
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


    # def test(self, bot, update):
    #     logging.info("Posting test toot...")
    #     new_toot_bot = TootBot("pytooter_clientcred.secret" , "pytooter_usercred.secret", self.website_base_url)
    #     new_toot_bot.send_new_meme(":acab: test toot, please ignore" , "images/test_kitten.jpg" , "unlisted")

    def start(self, bot, update):
        update.message.reply_text("I'm soon going to be up, a bit of patience...")

    def acab(self, bot, update):
        logging.info(str(update.message.chat.username) + " hates the police.")
        update.message.reply_text("fuck the police")

    def save_post_and_post_it(self, bot, update):
        logging.info("Got new work !")

        logging.info("Creating a new TootBot...")
        new_toot_bot = TootBot("pytooter_clientcred.secret" , "pytooter_usercred.secret", self.website_base_url)

        logging.info("Getting the caption...")
        if(update.channel_post.caption):
            caption = update.channel_post.caption
        else:
            caption = self.default_caption

        logging.info("Getting the file's id...")
        file_id = update.channel_post.photo[-1].file_id

        try:
            newFile = bot.get_file(file_id)
            file_path = "memes_tmp" + file_id + ".jpg"
            newFile.download(file_path)
        except Exception as e:
            logging.warn("Failed to down meme from telegram.")
            raise IOError
        try:
            new_toot_bot.send_new_meme(caption , file_path , "unlisted")
        except Exception as e:
            raise IOError
            return False
        try:
            os.remove(file_path)
        except Exception as e:
            logging.warn("The meme can't be deleted.")
            raise IOError

    def run(self):
        updater = Updater(self.bot_token)
        # updater.dispatcher.add_handler(CommandHandler('test', self.test))
        updater.dispatcher.add_handler(CommandHandler('acab', self.acab))
        updater.dispatcher.add_handler(CommandHandler('start', self.start))
        updater.dispatcher.add_handler(MessageHandler(Filters.photo & Filters.chat(self.channel_id) , self.save_post_and_post_it, channel_post_updates=True))
        updater.start_polling()
        updater.idle()
