from requests import *
import pytube
import re
import math
import youtube_dl

def download_message1():
    return "Gathering Sketches ⚙"

def download_message2():
    return "Forwarding Request to the Youtube Server 📡"

def  download_message3():
    return "Downloading ⬇️. . . ."

def tumbnail(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    id = link.split('=')
    thumbnail_url = 'https://img.youtube.com/vi/' + id[1] + '/maxresdefault.jpg'
    thumbnail = get(thumbnail_url).content
    return thumbnail

def video_title(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    title = video.title
    return title

def video_views(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    views = video.views
    return views

def video_length(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    length = round(video.length/60 , 2)
    length = str(length)+'min'
    return length

def video_age(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    if video.age_restricted == True:
        age = "18+"
    else:
        age = 'No restrictions available'
    return age


def validator(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    x = re.search("^https://.*youtube.com.*watch", link)
    if x:
        return "Link accepted"
    elif re.search("^https://.", link) :
        return "Oops! i'm curiously struggling with your link 😤😤, \nBecause it is not a *youtube* link"
    else:
        return "Oops! I'm blind on your message, I think it is not a link ☹️☹️\nProbably it would be a text"


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
def quality_size(link):
    args = link
    cnt = 1
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
    l = []
    t = []
    for i in video['formats']:
        if i['format_note'] not in l:
            l.append(i['format_note'])
            size = i['filesize']
            size_name = ("B", "KB", "MB", "GB", "TB")
            cal = int(math.floor(math.log(size, 1024)))
            p = math.pow(1024, cal)
            s = round(size / p, 2)
            t.append(f"{s} {size_name[cal]}")
    return l,t