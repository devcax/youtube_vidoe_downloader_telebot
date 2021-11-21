from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import *
import response as r
import constants as c
import downloader
import time as t

def start_command(update,context):


    user_name = update.message.chat.first_name
    update.message.reply_text(f"Hello {user_name}, how are you? Hope you are doing well💚💚 \nFirst thanks in advance for choosing me🤘🤘",quote=True)

    #res 1 with caption start command
    update.message.reply_photo('AgACAgUAAxkBAAIBIWGXX9L1NXm25yFxGSUSq_9fZeONAAJmrDEbzv-4VOUyN4KjhFb7AQADAgADcwADIgQ', caption = r.start_command_response)





def help_command(update,context):
    update.message.reply_text("Ok i'll help you")

    #res1 with caption help command
    update.message.reply_video("BAACAgUAAxkBAAIByGGXl7u4SLQr5980sCIV1RDnhKlpAAJ9AwACchq4VOtg0ZPgq0smIgQ",
                               caption=r.help_command_response)

def handle_message(update, context):
    text = str(update.message.text)
    if "download" in text.split():
        text = text.split()
        update.message.reply_text("Link Accepted ✅\nWorking on it . . .", quote=True)
        keyboard = [
            [
                InlineKeyboardButton("144p", callback_data='144p'),
                InlineKeyboardButton("240p", callback_data='240p'),
                InlineKeyboardButton("360p", callback_data='360p'),
            ],
            [
                InlineKeyboardButton("480p", callback_data='480p'),
                InlineKeyboardButton("720p", callback_data='720p'),
                InlineKeyboardButton("1080p", callback_data='1080p'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Choose a resolution at your own or default is 360p", reply_markup=reply_markup)
        t.sleep(5)
        update.message.reply_text(downloader.download_message1())
        t.sleep(1)
        update.message.reply_text(downloader.download_message2())
        t.sleep(1)
        update.message.reply_text(downloader.download_message3())

        #callback = reply_markup["inline_keyboard"]

        sts = downloader.Downloader(text[1],update.message.reply_markup)
        update.message.reply_text(sts)
        if sts == "Video Downloaded Successfully 🏆":
            update.message.reply_video(file_path="C:\\Users\\NIPUN\\PycharmProjects\\Telegrambot\\test.mp4")

    else:
        response = r.responses(text)
        if response == "unknown_input":
            update.message.reply_text("Oops What's this?, sorry i can't understand", quote=True)
        else:

            update.message.reply_text(response)


def time(update, context):
    time = r.time()
    update.message.reply_text(time)

def about(update, context):
    about = r.about()
    update.message.reply_text(about)

def kill(update, context):
    kill = r.kill()
    update.message.reply_text(kill)
    update.message.reply_sticker('CAACAgIAAxkBAAIBiGGXivEO8qoFjx9nCyFy0IOws-MbAAKkCQACeVziCRY25WGPnHY7IgQ')

def d_e_help(update, context):
    user_name = update.message.chat.first_name
    # down_error_help_ message
    update.message.reply_text(f"Dear {user_name}, i'm very sad about this,\nThis error can be occurs for many common resons\n",
                              r.down_error_help_response)

def pic(update,context):
    update.message.reply_text("Currently i'm not supporting on pictures/stickers",quote=True)




def error(update,context):
    print(f"Update {update} caused error {context.error}")



def main():
    updater = Updater(c.API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("end", kill))
    dp.add_handler(CommandHandler("download_error_help", d_e_help))

    dp.add_handler(MessageHandler(Filters.text,handle_message))
    dp.add_handler(MessageHandler(Filters.photo, pic))
    dp.add_handler(MessageHandler(Filters.sticker, pic))

    dp.add_handler(MessageHandler(Filters.video,pic))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()






