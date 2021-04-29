# Оповещение о пройденных уроках [devman](https://dvmn.org/modules/)

Скрипт слушает [devman API](https://dvmn.org/api/docs/) и при появлении 
проверенных работ отправляет уведомления в [Telegram](https://telegram.org/).


## Настройки

* Необходимо забрать персональный токен на сайте 
[devman API](https://dvmn.org/api/docs/).
 * Создать бота в Telegram через специального бота: 
[@BotFather](https://telegram.me/BotFather), забрать API ключ и написать 
созданному боту.
* Забрать свой `chat_id` через [@userinfobot](https://telegram.me/userinfobot).


Затем создать файл `.env` в корневой папке с кодом и записать туда токен, ключ, 
id в формате:
```
DEVMAN_TOKEN=ВАШ_DEVMAN_API_TOKEN
TG_NOTIFY_BOT_TOKEN=ВАШ_TELEGRAM_API_КЛЮЧ
TG_CHAT_ID=ВАШ_CHAT_ID
```

## Запуск

Для запуска у вас уже должен быть установлен [Python 3](https://www.python.org/downloads/release/python-379/).

- Скачайте код.
- Установите зависимости командой:
```
pip install -r requirements.txt
```
- Запустите скрипт командой: 
```
python main.py
```


