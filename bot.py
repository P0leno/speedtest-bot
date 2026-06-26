import time
import logging
import platform
from datetime import datetime

import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8981689466:AAGNzYFFvV2IP8wsvsibRUl7JsI8W0pQOgE"
START_TIME = datetime.now()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *SpeedTest Bot*\n\n"
        "Тестовый бот для проверки скорости ответа и отправки сообщений.\n\n"
        "*Доступные команды:*\n"
        "/ping — замерить скорость ответа бота\n"
        "/echo <текст> — повторить сообщение\n"
        "/uptime — время работы бота\n"
        "/speedtest — тест скорости интернета\n"
        "/info — информация о боте",
        parse_mode="Markdown",
    )


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start = time.time()
    msg = await update.message.reply_text("🏓 Pong...")
    elapsed = (time.time() - start) * 1000
    await msg.edit_text(f"🏓 Pong! `{elapsed:.1f} ms`", parse_mode="Markdown")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Использование: `/echo <текст>`", parse_mode="Markdown")
        return
    await update.message.reply_text(f"📢 {text}")


async def uptime(update: Update, context: ContextTypes.DEFAULT_TYPE):
    delta = datetime.now() - START_TIME
    total = int(delta.total_seconds())
    d, r = divmod(total, 86400)
    h, r = divmod(r, 3600)
    m, s = divmod(r, 60)
    await update.message.reply_text(f"⏱ Uptime: `{d}д {h}ч {m}м {s}с`", parse_mode="Markdown")


async def speedtest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await update.message.reply_text("⏳ Замер скорости...")
    url = "https://speedtest.tele2.net/5MB.zip"
    try:
        start = time.time()
        r = requests.get(url, stream=True, timeout=30)
        size = 0
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            size += len(chunk)
            if size >= 5 * 1024 * 1024:
                break
        elapsed = time.time() - start
        speed = (size * 8) / (elapsed * 1024 * 1024)
        await msg.edit_text(
            f"📥 *Download Speed*\n"
            f"Скорость: `{speed:.2f} Mbps`\n"
            f"Время: `{elapsed:.2f} с`\n"
            f"Объём: `{size / 1024 / 1024:.1f} MB`",
            parse_mode="Markdown",
        )
    except Exception as e:
        await msg.edit_text(f"❌ Ошибка: `{e}`", parse_mode="Markdown")


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🤖 *Bot Info*\n\n"
        f"🖥 Сервер: `{platform.node()}`\n"
        f"🐍 Python: `{platform.python_version()}`\n"
        f"⏱ Запущен: `{START_TIME.strftime('%Y-%m-%d %H:%M:%S')}`",
        parse_mode="Markdown",
    )


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("uptime", uptime))
    app.add_handler(CommandHandler("speedtest", speedtest))
    app.add_handler(CommandHandler("info", info))

    logger.info("Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
