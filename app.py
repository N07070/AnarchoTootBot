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
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.info("""

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    """)

    new_telegram_bot = TeleBot(import_config()[0], int(import_config()[1]), import_config()[2], import_config()[3])
    new_telegram_bot.run()

if __name__ == '__main__':
    main()
