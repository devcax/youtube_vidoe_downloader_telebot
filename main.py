import telegram
import youtube_dl
from telegram import *
import telebot
from telegram.ext import *
from requests import *
import pytube
import response as r
import constants as c
import downloader


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

bot = telebot.TeleBot(c.API_KEY)

def start_command(update,context):


    user_name = update.message.chat.first_name
    update.message.reply_text(f"Hello {user_name}, how are you? Hope you are doing well💚💚 \nFirst thanks in advance for choosing me🤘🤘",quote=True)

    #res 1 with caption start command
    update.message.reply_photo('AgACAgUAAxkBAAIBIWGXX9L1NXm25yFxGSUSq_9fZeONAAJmrDEbzv-4VOUyN4KjhFb7AQADAgADcwADIgQ', caption = r.start_command_response)





def help_command(update,context):
    update.message.reply_text("Ok i'll help you")

    #res1 with caption help command
    update.message.reply_video("BAACAgUAAxkBAAIIhGG0O-OK3RVC1TVzM-3VZO6lySHCAAI8BAACXBmgVaSY2CZzIogPIwQ",
                               caption=r.help_command_response)

query = "360p"


def query_handler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    print(query)


def reply_ids(message):
    cid = message.chat.id
    msg_id = message.message_id
    return cid,msg_id


def handle_message(update, context):
    text = str(update.message.text)
    if downloader.validator(text) == "Link accepted":

        text = text.split()

        update.message.reply_text("Link Accepted ✅\nWorking on it . . .", quote=True)
        keyboard = [
            [
                InlineKeyboardButton("144p 🎬", callback_data='144p'),
                InlineKeyboardButton("240p 🎬", callback_data='240p'),
                InlineKeyboardButton("360p 🎬", callback_data='360p'),
            ],
            [
                InlineKeyboardButton("480p 🎬", callback_data='480p'),
                InlineKeyboardButton("720p 🎬", callback_data='720p'),
                InlineKeyboardButton("1080p 🎬", callback_data='1080p'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Choose a resolution at your own or default is 360p", reply_markup=reply_markup)

        #Youtubevideo downloader
        def download(link):
            args = link
            cnt = 1
            try:
                with ydl:
                    result = ydl.extract_info(
                        args,
                        download=False  # We just want to extract the info
                    )
                if 'entries' in result:
                    # Can be a playlist or a list of videos
                    video = result['entries'][0]
                else:
                    # Just a video
                    video = result

                for i in video['formats']:
                    link = '<a href=\"' + i['url'] + '\">' + 'Download ⬇️' + '</a>'
                    if i.get('format_note'):
                        if i['format_note'] == query:
                            link_message = update.message.reply_photo(downloader.tumbnail(args), caption=f"\nVideo Title :-  {downloader.video_title(args)}\n"
                                                                                          f"👁‍🗨 Views :- {downloader.video_views(args)}\n"
                                                                                          f"⛳️Length :- {downloader.video_length(args)}\n "
                                                                                          f"🔞 Age Restrictions :- {downloader.video_age(args)}\n"
                                                                                          f"🎬 Quality :- {query}\n"
                                                                                          f"Downloadable Link {cnt} :- {link}",parse_mode='HTML')
                            update.message.reply_text("❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌")
                            '''
                            keyboard = [
                                [
                                    InlineKeyboardButton("Next Link>> ", callback_data='next')

                                ]

                            ]
                            reply_markup = InlineKeyboardMarkup(keyboard)

                            update.message.reply_text("❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌",
                                                      reply_markup=reply_markup)
                            '''
                            cnt += 1
                            continue

                    else:
                        update.message.reply_text(link, parse_mode='HTML', disable_notification=True)
                update.message.reply_text("Done ✅")


            except:
                context.bot.send_message('Error occurs while downloading  /download_error_help')
            # Youtubevideo downloader end

        download(text[1])
    else:
        update.message.reply_text(downloader.validator(text))


def time(update, context):
    global t_counter
    time = r.time()
    update.message.reply_text(time)


def about(update, context):
    about = r.about()
    update.message.reply_text(about,parse_mode='HTML')

def kill(update, context):
    kill = r.kill()
    update.message.reply_text(kill)
    update.message.reply_sticker('CAACAgIAAxkBAAIBiGGXivEO8qoFjx9nCyFy0IOws-MbAAKkCQACeVziCRY25WGPnHY7IgQ')
    # forwarded to query handler function



def d_e_help(update, context):

    user_name = update.message.chat.first_name
    print("yes")
    update.message.reply_text(f"Dear {user_name}, i'm very sad about this,\nThis error can be occurs for many common resons\n"
                              f"{r.down_error_help_response}")

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

    dp.add_handler(CallbackQueryHandler(query_handler))


    dp.add_handler(MessageHandler(Filters.video,pic))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()






