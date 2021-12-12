from requests import *
import pytube
import re
import math


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

def video_file_size(link,res='360p'):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    size = video.streams.get_by_resolution(res).filesize_approx
    if size == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return "%s %s" % (s, size_name[i])

def validator(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
        print(link)
    x = re.search("^download.https://.*youtube.com.*watch", link)
    if "download" in link.split():
        try:
            if link.split()[1]:
                if x:
                    return "Link accepted"
                else:
                    return "Invalied Link"
        except IndexError:
            return "Link is missing"

    else:
        return "'download' Prefix is misiing"

def get_resfor_eachquality(link):
    if 'youtu.be' in link.split('/'):
        link = f"{link.split('/')[0]}//www.youtube.com/watch?v={link.split('/')[3]}"
    video = pytube.YouTube(link)
    res = ['144p','240p','360p','480p','720p','1080p']
    quality = []
    for i in res:
        try:
            size = video.streams.get_by_resolution(i).filesize_approx
        except:
            quality.append("not available")
            continue
        if size == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size, 1024)))
        p = math.pow(1024, i)
        s = round(size / p, 2)
        quality.append(f"{s}{size_name[i]}")
    return quality