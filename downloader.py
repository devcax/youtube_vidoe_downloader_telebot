from pytube import YouTube


def download_message1():
    return "Gathering Sketches ⚙"

def download_message2():
    return "Forwarding Request to the Youtube Server 📡"

def  download_message3():
    return "Downloading ⬇️. . . ."


def Downloader(link,reslution="360p"):
    try:
        Video_Url = YouTube(str(link))
        Video = Video_Url.streams.filter(res=f"{reslution}").first()
        Video.download()
        return "Video Downloaded Successfully 🏆"
    except:
        return "Something Went Wrong"

