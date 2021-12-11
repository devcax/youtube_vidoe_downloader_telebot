from datetime import *
from pytube import YouTube

start_command_response =   "Who am I \n\n" \
                           "📌 I'm an Utube video downloading bot🤖.\n" \
                           "📌 You can use me to download⏬ any Utube \n       video, which is located in the youtube\n       servers.\n" \
                           "📌 The Only thing you want to do is send me\n       your desired video link with the 'download'\n       prefix" \
                           "\neg:- download https://yourdesiredutubevideo.link\n\n" \
                           "👀Still don't know how to use me ok don't worry\n" \
                           "/help click on this"

help_command_response = "🔄Go through this video and learn how to use me\n\n"\
                        "#tutoroals | #telegram | #help"

down_error_help_response = f"\nRead Followings and try to troubleshoot your problem\n"\
                           f"○ Invalid link - Link may be broken\n"\
                           f"○ Fault - Inline system failure\n"\
                           f"○ Download request failed - 'https://' is missing\n"\
                           f"○ Download request forced - 'You may not\n    entered link properly or completly mssing the\n    link\n"\
                           f"○ Download request denied - Probably your\n    trying video is a private video"

def responses(message):
    user_message = str(message).lower().strip("? ! @ # $ % ^ & * ( )")
    user_message_list = message.split()
    print(user_message_list)
    if user_message in ("hello","hi","hey"):
        return "Hi, How it's going there?"
    if user_message in ('who are you','what is your name',"Who is you"):
        return "Im a AI Chatbot"
    if user_message in ('who made you','who is the creator of you',"Who is you"):
        return "Im a AI Chatbot"
    if user_message in ('time',"can you tell me time","What is the time now"):
        return "ah Yes! \nToday is:- "+datetime.now().strftime("%x")+"\nExact time:-"+datetime.now().strftime("%X")

    if "download" in user_message_list:
        if "https://" in user_message:
            link = user_message_list[1]
            url = YouTube(str(link))
            video = url.streams.first()
            video.download()
            return "Done"

        else:
            return "Invalid link (broken link) or you haven't entered a link with 'download' prefix\n" \
                   "/download_error_help"

    return "unknown_input"

def time():
    return "ah Yes! \n🕐Today is:- " + datetime.now().strftime("%x") + "\n🕐Time:-" + datetime.now().strftime("%X")

def about():
    p = "ABOUT ME\n\n" \
           f"○ Creator : ภĮℙⓤ𝐧 \n"\
           "○ Cloud : Github, Heroku cloud \n"\
           "○ Language : Python  \n"\
           "○ Library : Telegram-bot-module \n"\

    return p
def kill():
    return "Bye! 👋🏻" \
           "\nHave a Nice Day . . . "