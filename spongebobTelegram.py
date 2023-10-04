from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import time
updater = Updater(token='5726063980:AAHgzgmfQhGhSbSfxdgAAHlaBUW4ueR8g2w')

import requests
TOKEN = "5726063980:AAHgzgmfQhGhSbSfxdgAAHlaBUW4ueR8g2w"
chat_id = "5940040611"
# message = "hello from your telegram bot"
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# requests.get(url).json()

# bot = telegram.Bot(TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "")

def receiver(update: Update, context: CallbackContext):
    global textFromUser
    global needPrompt
    needPrompt = False
    textFromUser = update.message.text

def getInput():
    global needPrompt
    needPrompt = True

    while True: 
        updater.dispatcher.add_handler(MessageHandler(Filters.text, receiver))
        updater.start_polling()
        try:
            if needPrompt == True:
                # print("prompt needed")
                time.sleep(2)
                raw_text = textFromUser
            if needPrompt == False:
                # print("prompt not needed")
                # time.sleep(2)

                return raw_text
        except (Exception) as e:
            pass

# ml portion
def run():
    history = []
    while True:
        raw_text = getInput()
        if not textFromUser:
            raw_text = getInput()
        message = raw_text + "some"    
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url).json()

run()
