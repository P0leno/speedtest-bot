# SpeedTest Bot

Telegram-бот для тестирования скорости ответа, интернет-соединения и отправки сообщений.

## Быстрый старт через Docker (одна команда)

```bash
git clone https://github.com/P0leno/speedtest-bot && cd speedtest-bot && docker compose up -d
```

Бот запустится в контейнере и автоматически перезапускается при падении (`restart: unless-stopped`).

Остановить:

```bash
docker compose down
```

## Запуск без Docker

```bash
git clone https://github.com/P0leno/speedtest-bot && cd speedtest-bot && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python bot.py
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

- [Docker](https://docs.docker.com/engine/install/) (для Docker-запуска)
- Или Python 3.8+ (для запуска без Docker)
