from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import bot_token
import os
from dotenv import load_dotenv

import requests
load_dotenv()
SERVER_ADDRESS = os.getenv('SERVER_ADDRESS')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! This is your bot.')

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get(f"{SERVER_ADDRESS}/data")
    if response.status_code == 200:
        data = response.json()
        await update.message.reply_text(data.get("message", "No message found"))
    else:
        await update.message.reply_text("Failed to fetch data from server.")

def main():
    # Create the Application and pass it your bot's token
    application = Application.builder().token(bot_token.BOT_TOKEN).build()

    # Register the /start command with the start function
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    test_handler = CommandHandler('test', test)
    application.add_handler(test_handler)

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()