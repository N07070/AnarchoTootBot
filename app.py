#!bin/python

from TeleBot import TeleBot
import configparser, logging


def import_config():
    config = configparser.ConfigParser()
    config.read('config.conf')
    config_vars = []
    config_vars.append(config['telegram_bot']['telegram_bot_token'])
    config_vars.append(config['telegram_bot']['channel_to_watch'])
    config_vars.append(config['mastodon_bot']['website_url'])
    config_vars.append(config['mastodon_bot']['default_caption'])

    return config_vars

def main():
    new_telegram_bot = TeleBot(import_config()[0], int(import_config()[1]), import_config()[2], import_config()[3])
    new_telegram_bot.run()

if __name__ == '__main__':
    main()
