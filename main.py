import youtube_dl # to download and generate youtube downloader link
from telegram import * # main telegram module 1
from telegram.ext import * # main telegram module 2
import response as r
import constants as c
import downloader


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

###################################################################################################
# command handlers

def start_command(update,context):
    user_name = update.message.chat.first_name
    k = update.message.reply_text(f"*Hello {user_name}, how are you? Hope you are doing well💚💚 \nFirst thanks in advance for choosing me🤘🤘*",quote=True, parse_mode= 'Markdown')
    #res 1 with caption start command
    update.message.reply_photo('AgACAgUAAxkBAAMaYbWZcWM1CyCumo-9vyrG71yI03QAAi6vMRu3GKlVNiefBUEPJwUBAAMCAANzAAMjBA', caption =f'*{r.start_command_response}*',parse_mode= 'Markdown')

def help_command(update,context):
    # help text
    update.message.reply_text("*Ok i'll help you*", parse_mode= 'Markdown')

    # help video
    update.message.reply_video("BAACAgUAAxkBAAMfYbWZsK32U9ppc_M3Kv6GnVGlEMQAAjwEAAJcGaBVJKwNfr5W3b0jBA",
                               caption=f'*{r.help_command_response}*',parse_mode= 'Markdown')

def time(update, context):
    global t_counter
    time = r.time()
    keyboard = [[
            InlineKeyboardButton(f"❌ Close ❌ ", callback_data='close'),
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"*{time}*", reply_markup=reply_markup, parse_mode= 'Markdown')


def about(update, context):
    about = r.about()
    keyboard = [
        [
            InlineKeyboardButton(f"👨‍👧‍👦 Sibling bots", callback_data='s_bots'),
            InlineKeyboardButton(f"💰 Donate ",callback_data='donate'),

        ],[
            InlineKeyboardButton(f"📞 Contact the creator", url='https://t.me/NippuN90'),
        ],
        [
            InlineKeyboardButton(f"❌ Close ❌ ", callback_data='close'),
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text=f'*{about}*', reply_markup=reply_markup,parse_mode= 'Markdown')


def setting(update, context):
    keyboard = [
        [
            InlineKeyboardButton(f"🇰🇾 English (DEF)", callback_data='en'),
            InlineKeyboardButton(f"🇱🇰 Sinhala ", callback_data='sin'),

        ],[
            InlineKeyboardButton(f"❌ Close ❌ ", callback_data='close'),
        ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("*Select your preferred Language*", reply_markup=reply_markup, parse_mode= 'Markdown')
    # forwarded to query handler function



def d_e_help(update, context):

    user_name = update.message.chat.first_name
    print("yes")
    update.message.reply_text(f"*Dear {user_name}, i'm very sad about this,\nThis error can be occurs for many common resons\n*"
                              f"*{r.down_error_help_response}*",parse_mode= 'Markdown')

# command handler end

###################################################################################################

# if user sends a pic following code will execute

def pic(update,context):
    p = update.message.reply_text("Currently i'm not supporting on pictures/stickers",quote=True)
    print(p)
# if user sends a pic following code will execute end

###################################################################################################

# if error occurs it will print in the idle

def error(update,context):
    print(f"Update {update} caused error {context.error}")

# if error occurs it will print in the idle end

###################################################################################################
query = "360p"


###################################################################################################
# chat id & message id

def chat_id(message):
    return message.chat.id

def msg_id(message):
    return message.message_id

# chat id & message id end
###################################################################################################

# query & message handlers
default_video_quality = '360p'
def query_handler(update: Update, context: CallbackContext):
    global default_video_quality
    query = update.callback_query.data
    if query == 'sin':
        update.callback_query.answer("Language switched to 'Sinhala'")
        update.callback_query.edit_message_text('Language Updated Successfully')
    elif query=='en':
        update.callback_query.answer("Language switched to 'English'")
        update.callback_query.edit_message_text('Language Updated Successfully')
    elif query=='close':
        update.callback_query.delete_message()
    elif query == 's_bots':
        update.callback_query.answer('We are currently working on new bots')
    elif query == '360p':
        default_video_quality = '360p'
    elif query == '720p':
        default_video_quality = '720p'
    print(query)


def message_handler(update, context):
    text = str(update.message.text)
    if downloader.validator(text) == "Link accepted":

        text = text.split()

        update.message.reply_text("Link Accepted ✅\nWorking on it . . .", quote=True)
        keyboard = [
            [
                InlineKeyboardButton(f"144p 🎬 ({downloader.get_resfor_eachquality(text[1])[0]})", callback_data='144p'),
                InlineKeyboardButton(f"240p 🎬 ({downloader.get_resfor_eachquality(text[1])[1]})", callback_data='240p'),
                InlineKeyboardButton(f"360p 🎬 ({downloader.get_resfor_eachquality(text[1])[2]})", callback_data='360p'),
            ],
            [
                InlineKeyboardButton(f"480p 🎬 ({downloader.get_resfor_eachquality(text[1])[3]})", callback_data='480p'),
                InlineKeyboardButton(f"720p 🎬 ({downloader.get_resfor_eachquality(text[1])[4]})", callback_data='720p'),
                InlineKeyboardButton(f"1080p 🎬 ({downloader.get_resfor_eachquality(text[1])[5]})", callback_data='1080p'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text("Choose a resolution at your own or default is 360p", reply_markup=reply_markup)
        #Youtubevideo downloader start YOUTUBE_DL

        def download(link):

            downloadable_link = ''
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
                    # if Just a video
                    video = result

                for i in video['formats']:
                    link = f'Downloadable Link {cnt} :- '+'<a href=\"' + i['url'] + '\">' + 'Download ⬇️' + '</a>\n'
                    if i.get('format_note'):

                        if i['format_note'] == default_video_quality:
                            downloadable_link += link
                            cnt += 1

                    else:
                        update.message.reply_text(link, parse_mode='HTML', disable_notification=True)
                update.message.reply_photo(downloader.tumbnail(args),
                                           caption=f"\nVideo Title :-  {downloader.video_title(args)}\n"
                                                   f"👁‍🗨 Views :- {downloader.video_views(args)}\n"
                                                   f"⛳️Length :- {downloader.video_length(args)}\n "
                                                   f"🎥 File Size :- {downloader.video_file_size(args,default_video_quality)}\n"
                                                   f"🔞 Age Restrictions :- {downloader.video_age(args)}\n"
                                                   f"💡 Language :- en-us\n"
                                                   f"🎬 Quality :- {query}\n"
                                                   f"💿 Format :- webm/mp4\n"
                                                   f"{downloadable_link}", parse_mode='HTML')
                update.message.reply_text("❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌🔆❌")
                update.message.reply_text("Done ✅")


            except:
                update.message.reply_text('Error occurs while downloading  /download_error_help')
            # Youtube video downloader end YOUTUBE_DL

        download(text[1])
    else:
        update.message.reply_text(downloader.validator(text))

# query & message handlers end
###################################################################################################


def main():

    updater = Updater(c.API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("settings", setting))
    dp.add_handler(CommandHandler("download_error_help", d_e_help))

    dp.add_handler(MessageHandler(Filters.text,message_handler))
    dp.add_handler(MessageHandler(Filters.photo, pic))
    dp.add_handler(MessageHandler(Filters.sticker, pic))

    dp.add_handler(CallbackQueryHandler(query_handler))


    dp.add_handler(MessageHandler(Filters.video,pic))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()






