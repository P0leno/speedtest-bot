# SpeedTest Bot

Telegram-бот для тестирования скорости ответа, интернет-соединения и отправки сообщений.

## Быстрый старт (одна команда)

```bash
git clone https://github.com/P0leno/speedtest-bot && cd speedtest-bot && pip install -r requirements.txt && python bot.py
```

Запуск на сервере (в фоне):

```bash
git clone https://github.com/P0leno/speedtest-bot && cd speedtest-bot && pip install -r requirements.txt && nohup python bot.py > bot.log 2>&1 &
```

## Команды

| Команда | Описание |
|---------|----------|
| `/start` | Приветствие и список команд |
| `/ping` | Замер времени ответа бота (ms) |
| `/echo <текст>` | Повторяет отправленный текст |
| `/uptime` | Время работы бота |
| `/speedtest` | Тест скорости загрузки (Mbps) |
| `/info` | Информация о сервере и боте |

## Требования

- Python 3.8+
- Telegram Bot Token (уже встроен в `bot.py`)
