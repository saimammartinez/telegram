import telegram
from telegram.ext import *

mibot = telegram.Bot(token="578548370:AAG76e31bbO1nH_lj_0ePL2XTUam7GambJM")

mibot_uptader = Updater(mibot.token)

def start(bot, update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="Gracias por usar este bot!!")

def judith(bot, update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola profe chunga!!! ")


start_handler = CommandHandler('judith', judith)

dispatcher = mibot_uptader.dispatcher

dispatcher.add_handler(start_handler)

mibot_uptader.start_polling()
mibot_uptader.idle()

while True:
    pass
