from telegram import Bot
import os
from random import shuffle
import time
from dotenv import load_dotenv


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
                if os.path.getsize(file_path) <= max_file_size:
                    with open(f'{folder_name}/{file}', 'rb') as photo_file:
                        bot.send_photo(chat_id=channel_name, photo=photo_file)
                time.sleep(int(sleeping_time))
    
    
if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    sleeping_time = os.environ["TIME"]
    folder_name = os.environ["IMAGE_NAME_FOLDER"]
    channel_name = os.environ["TELEGRAM_CHANNEL_NAME"]
    send_on_telegram(bot_token, folder_name, channel_name,sleeping_time)
