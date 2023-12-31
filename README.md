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

- `NASA_API_TOKEN`=Ваш_API_токен
- `IMAGE_NAME_FOLDER`=имя_папки_с_изображениями
- `NUMBER_DAYS`=количество_дней
- `START_DATE`=начальная_дата
- `TELEGRAM_BOT_TOKEN`=Токен_вашего_бота
- `TIME`=время_отправки
- `TELEGRAM_CHANNEL_NAME`=имя_вашего_канала

### telegram_boot.py script
Этот скрипт предназначен для отправки изображений из локальной директории в Telegram-канал через регулярные интервалы. Он проверяет, что изображения соответствуют лимиту размера файлов Telegram перед отправкой.
```bash
    python  telegram_boot.py 
```
### get_image.py script
Этот скрипт разработан для получения последних космических изображений от разных источников, таких как SpaceX и NASA. Он интегрируется с публичным API SpaceX для получения изображений с последнего запуска и сервисов NASA APOD (Astronomy Picture of the Day) и EPIC (Earth Polychromatic Imaging Camera) для сбора потрясающих космических фотографий.
```bash
    python  get_image.py --id SPACEX_LAUNCH_ID
```

Замените script_name.py на имя вашего скрипта и SPACEX_LAUNCH_ID на желаемый ID запуска SpaceX, если вы хотите указать другой запуск.  

### get_nasa_picture.py script
Написана функция **get_nasa_pictures**,которая получает изображения от NASA Astronomy Picture of the Day (APOD) API и сохраняет их на вашем локальном компьютере.
### fetch_spacex_images.py script
Написана функция **fetch_spacex_image**, которая получает изображения с последнего запуска SpaceX и сохраняет их на вашем локальном компьютере.

### get_epic.py script
Написана функция **get_epic** предназначен для получения изображений от NASA's EPIC (Earth Polychromatic Imaging Camera) API за заданное количество дней и сохраняет их на вашем локальном компьютере.

### process_image.py script
Данный скрипт является вспомогательных для скачивания и получения разрешений фотографий.







