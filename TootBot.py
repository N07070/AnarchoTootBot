from mastodon import Mastodon
import os, logging

class TootBot(object):
    """Sends toots to Mastodon"""

    def __init__(self, client_id_file, access_token_file, mastodon_instance):
        super(TootBot, self).__init__()
        self.mastodon = Mastodon( client_id = client_id_file , access_token = access_token_file , api_base_url = mastodon_instance)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


    def send_new_meme(self, toot_text,image_path, visibility_of_toot):
        # Upload the image of the meme
        if len(toot_text) > 499:
            toot_text = toot_text[:496] + "..."

        if not os.path.isfile(image_path):
            logging.warn("The file that I tried to upload does not exists. Exiting.")
            raise IOError
            return False

        try:
            media_id_of_post = self.mastodon.media_post(image_path, description=toot_text)
        except Exception as e:
            logging.warn("Cannot upload the meme to mastodon.")
            raise IOError
            return False

        try:
            self.mastodon.status_post(toot_text,
                                    in_reply_to_id=None,
                                    media_ids=[media_id_of_post],
                                    sensitive=False,
                                    visibility=visibility_of_toot,
                                    spoiler_text=None)
            logging.info("Posted a new meme to Mastodon !")
        except Exception as e:
            raise IOError
            return False
