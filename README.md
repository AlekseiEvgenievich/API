# AstroImages Bot

Этот проект предназначен для автоматической публикации изображений в Telegram канале.

## Окружение и зависимости

- **Python**: 3.10+
- **Telegram API**: Необходимо иметь активный бот и знать его токен.


## Установка зависимостей

Чтобы установить все необходимые зависимости, выполните:

```bash
pip install -r requirements.txt
```

## Настройка

1. Создайте `.env` файл в корне вашего проекта.
2. Установите следующие переменные:

- `API_TOKEN`=Ваш_API_токен
- `NAME_FOLDER`=имя_папки_с_изображениями
- `NUMBER_DAYS`=количество_дней
- `START_DATE`=начальная_дата
- `BOT_TOKEN`=Токен_вашего_бота
- `TIME`=время_отправки
- `CHANNEL_NAME`=имя_вашего_канала

### get_nasa_picture.py script
This script fetches images from the NASA Astronomy Picture of the Day (APOD) API and saves them to your local machine.
### fetch_spacex_images.py script
This script fetches images from the latest SpaceX launch and saves them to your local machine.
### get_epic.py script
This script is designed to fetch images from NASA's EPIC (Earth Polychromatic Imaging Camera) API for the given number of days and saves them to your local machine.
### telegram_boot.py script
This script is designed to send images from a local directory to a Telegram channel at regular intervals. It ensures the images are within Telegram's file size limit before sending.
### get_imageinformation.py script
This script is developed to fetch the latest space-related images from multiple sources like SpaceX and NASA. It integrates with SpaceX's public API to fetch the latest launch images and NASA's APOD (Astronomy Picture of the Day) and EPIC (Earth Polychromatic Imaging Camera) services to gather astonishing space photos.
```bash
    python  get_imageinformation.py --id SPACEX_LAUNCH_ID
    ```

    Replace `script_name.py` with the name of your script and `SPACEX_LAUNCH_ID` with the desired SpaceX launch ID if you want to specify a different launch.





