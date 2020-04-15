import youtube_dl
import os
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import webbrowser
choice_lsto = ['youtube', 'net', 'online', 'browser', 'chrome']
choice_lstpc = ['pc', 'computer', 'laptop', 'download', 'download it', 'downloadit']


def song_file_path():
    path = 'D:/movies/'
    folder = path
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
        return path


def play_song(mysong):
    path = song_file_path()
    if mysong:
        flag = 0
        url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
        response = urlopen(url)
        html = response.read()
        soup1 = soup(html, "lxml")
        url_list = []
        for vid in soup1.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                flag = 1
                final_url = 'https://www.youtube.com' + vid['href']
                url_list.append(final_url)
        try:
            url = url_list[0]
            return url
        except:
            return None
            pass
def play_video(myvideo):
    path = song_file_path()
    if myvideo:
        flag = 0
        url = "https://www.youtube.com/results?search_query=" + myvideo.replace(' ', '+')
        response = urlopen(url)
        html = response.read()
        soup1 = soup(html, "lxml")
        url_list = []
        for vid in soup1.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                flag = 1
                final_url = 'https://www.youtube.com' + vid['href']
                url_list.append(final_url)
        try:
            url=[]
            for i in range(5):
                url.append(url_list[i])
            return url
        except:
            return None
            pass
def play(url,choice):
    path = song_file_path()
    if choice in choice_lsto:
        webbrowser.open(url)
    elif choice in choice_lstpc:
        ydl_opts = {}
        os.chdir(path)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            p = os.listdir(path)
            path = path + p[0]
            os.startfile(path)

