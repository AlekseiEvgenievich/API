from telegram import Bot
import os
from random import shuffle
import time
from dotenv import load_dotenv


def get_file_size(file_path):
    """Get the file size in bytes."""
    return os.path.getsize(file_path)


def send_on_telegram(bot_token, folder_name, channel_name,sleeping_time):
        max_file_size = 20 * 1024 * 1024
        bot = Bot(token=bot_token)
        name_of_files = []
        for dirpath, dirnames, filenames in os.walk(folder_name):
            for file_name in filenames:
                name_of_files.append(file_name)
        while True:
            shuffle(name_of_files)
            for file in name_of_files:
                file_path = '{}/{}'.format(folder_name,file)
                if get_file_size(file_path) <= max_file_size:
                    bot.send_photo(chat_id=channel_name, photo=open('{}/{}'.format(folder_name,file), 'rb'))
                time.sleep(int(sleeping_time))
    
    
if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ["BOT_TOKEN"]
    sleeping_time = os.environ["TIME"]
    folder_name = os.environ["NAME_FOLDER"]
    channel_name = os.environ["CHANNEL_NAME"]
    send_on_telegram(bot_token, folder_name, channel_name,sleeping_time)
