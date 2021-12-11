from requests import *
import pytube
import re

def download_message1():
    return "Gathering Sketches ⚙"

def download_message2():
    return "Forwarding Request to the Youtube Server 📡"

def  download_message3():
    return "Downloading ⬇️. . . ."

def tumbnail(link):
    id = link.split('=')
    thumbnail_url = 'https://img.youtube.com/vi/' + id[1] + '/maxresdefault.jpg'
    thumbnail = get(thumbnail_url).content
    return thumbnail

def video_title(link):
    video = pytube.YouTube(link)
    title = video.title
    return title

def video_views(link):
    video = pytube.YouTube(link)
    views = video.views
    return views

def video_length(link):
    video = pytube.YouTube(link)
    length = round(video.length/60 , 2)
    length = str(length)+'min'
    return length

def video_age(link):
    video = pytube.YouTube(link)
    if video.age_restricted == True:
        age = "18+"
    else:
        age = 'No restrictions available'
    return age

def validator(link):
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