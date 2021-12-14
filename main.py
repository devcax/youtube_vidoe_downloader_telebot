import youtube_dl # to download and generate youtube downloader link
from telegram import * # main telegram module 1
from telegram.ext import * # main telegram module 2
import response as r
import constants as c
import downloader




ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})


def download(link,update,context,default_video_quality):
    global a,b,size
    downloadable_link = ''
    args = link
    cnt = l_cnt = 1
    # try:
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
        link = f'Downloadable Link {l_cnt} :- ' + '<a href=\"' + i['url'] + '\">' + 'Download ⬇️' + '</a>\n'

        if i.get('format_note'):

            if i['format_note'] == default_video_quality:
                if cnt == 1:
                    t = update.message.reply_photo(downloader.tumbnail(args), caption='Downloading . . .')
                if i['ext'] == 'mp4':
                    downloadable_link += link
                    l_cnt += 1
                cnt += 1
        else:
            update.message.reply_text(link, parse_mode='HTML', disable_notification=True)
    q_dic = {'tiny': 0, '144p': 1, '240p': 2, '360p': 3, '480p': 4, '720p': 5, '1080p': 6, '1440p': 7, '2160p': 8}
    context.bot.edit_message_media(message_id=msg_id(t), chat_id=chat_id(t),
                                   media=InputMediaPhoto(media=f'{t.photo[1].file_id}',
                                                         caption=f"\nVideo Title :-  {downloader.video_title(args)}\n"
                                                                 f"👁‍🗨 Views :- {downloader.video_views(args)}\n"
                                                                 f"⛳️Length :- {downloader.video_length(args)}\n "
                                                                 f"🎥 File Size :- {size[q_dic[default_video_quality]]}\n"
                                                                 f"🔞 Age Restrictions :- {downloader.video_age(args)}\n"
                                                                 f"💡 Language :- en-us\n"
                                                                 f"🎬 Quality :- {default_video_quality}\n"
                                                                 f"💿 Format :- mp4\n"
                                                                 f"{downloadable_link}", parse_mode='HTML'
                                                         )
                                   )

    update.message.reply_text("*Done ✅\n"
                              "#youtube | #bot | #download*", parse_mode='Markdown')
    context.bot.deleteMessage(message_id=msg_id(a), chat_id=chat_id(a))
    context.bot.deleteMessage(message_id=msg_id(b), chat_id=chat_id(b))


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
            InlineKeyboardButton("🇰🇾 English (DEF)", callback_data='en'),
            InlineKeyboardButton("🇱🇰 Sinhala ", callback_data='sin'),

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
query = "720p"


###################################################################################################
# chat id & message id

def chat_id(message):
    return message.chat.id

def msg_id(message):
    return message.message_id

# chat id & message id end
###################################################################################################

# query & message handlers
def query_handler(update: Update, context: CallbackContext):
    global text,updatee,contextt
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
    elif query == 'tiny':
        download(text, updatee, contextt, "tiny")
    elif query == '144p':
        download(text, updatee, contextt, "144p")
    elif query == '240p':
        download(text, updatee, contextt, "240p")
    elif query == '360p':
        download(text, updatee, contextt, "360p")
    elif query == '480p':
        download(text, updatee, contextt, "480p")
    elif query == '720p':
        download(text, updatee, contextt, "720p")
    elif query == '1080p':
        download(text, updatee, contextt, "1080p")
    elif query == '1440p':
        download(text, updatee, contextt, "1440p")
    elif query == '2160p':
        download(text, updatee, contextt, "2160p")
    #print(query)


def message_handler(update, context):
    global a,b,text,updatee,contextt,size
    updatee = update
    contextt = context
    text = str(update.message.text)
    if downloader.validator(text) == "Link accepted":
        a = update.message.reply_text("Link Accepted ✅\nWorking on it . . .", quote=True)
        try:
            quality,size = downloader.quality_size(text)
            count = 0
            keyboard = []
            for z in quality:
                if count < len(quality)-1:
                    keyboard.append([
                    InlineKeyboardButton(f'{quality[count]} 🎬 ({size[count]})', callback_data=f'{quality[count]}'),
                    InlineKeyboardButton(f'{quality[count + 1]} 🎬 ({size[count+1]})', callback_data=f'{quality[count+1]}'),
                        ])
                    count +=2
                    continue
                break
            reply_markup = InlineKeyboardMarkup(keyboard)

            b = update.message.reply_text("Choose a resolution ✨ ", reply_markup=reply_markup)
        except:
            update.message.reply_text("*Download Failed 🙁\nvideo duration too long . . .* ",parse_mode= 'Markdown')

    else:
        update.message.reply_text(f"{downloader.validator(text)}\n\n *URL* :- {text} ",parse_mode= 'Markdown')

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






