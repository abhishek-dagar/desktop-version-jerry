# import libraries
from speech_recog import *
import pyttsx3
from time import strftime
import wikipedia
import re
from google import google
import os
import fb
import datetime
from pyowm import OWM
import requests
import webbrowser
import sendsms
import movie_downloader
import game_downloader
import player
import ctypes
import json
import search_file
from pynput.keyboard import Controller
from taskmanger import open_apps,close_app
import time

keyboard = Controller()
# DICTIONRIES
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which'}
goodbye_lst = ['goodbye', 'bye', 'see you again']
choice_dict ={'first':1,'second':2,'third':3,"fourth":4,"fifth":5,'forth':4,'fort':4}
choice_list = ['first','second','third',"fourth","fifth",'forth','fort']
open_launch_dict = {'open': 'open', 'launch': 'launch'}




# TO check search is valid or not
def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True



def weather_info(command):
    reg_ex = re.search('current weather in (.*)', command)
    if reg_ex:
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = reg_ex.group(1)
        url = api_address + city
        json_data = requests.get(url).json()
        weather_info = json_data['weather'][0]['main'].lower()
        weather_temp = json_data['main']['temp']
        weather_temp = round(weather_temp - 273.15,2)
        speak(
                'Current weather in %s is %s. The maximum temperature is %0.2f degree celcius' % (
                city, weather_info,weather_temp))
# TO SPEAK
def speak(msg):
    engine = pyttsx3.init()
    engine.say('{}'.format(msg))
    engine.runAndWait()


# for aking from google
def tellabout(command):
    reg_ex = re.search('tell me about (.*)', command)
    try:
        if reg_ex:
            topic = reg_ex.group(1)
            ny = wikipedia.page(topic)
            print(ny)
            speak(ny.content[:50].encode('utf-8'))
    except Exception as e:
        print(e)
        speak(e)


# Wishme function
def wishme():
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak('Hello Sir. Good morning')
    elif 12 <= day_time < 18:
        speak('Hello Sir. Good afternoon')
    else:
        speak('Hello Sir. Good evening')


def run(command):
    if command.replace("computer","").strip()=="":
        command = myCommand().lower()
    else:
        command=command.replace("computer","")
    if 'tell me about' in command:
        command=command.replace("tell me about","")
        tellabout(command)
    elif 'who create you 'in command:
        speak("by abhishek")
    elif is_valid_google_search(command):
        print('in google search...')
        speak('in google search...')
        search_result = google.search(command)
        for result in search_result:
            print(result.description.replace('...', '').rsplit('.', 5)[0])
            if result.description != '':
                result = result.description.replace('...', '').rsplit('.', 5)[0]
                speak(result)
            break

    elif "open" in command or "launch" in command:
            if 'file' in command:
                print('In opening...')
                speak('opening...')
                key = command.replace('open ', '').replace('launch ', '')
                key=key.replace('file','')
                print('Key is : ' + key)
                search_file.set_root("D:\\")
                files = search_file.searchFile(key)
                speak("i found %d file" % len(files))
                for file in files:
                    file=file.split
                speak("which you want to open")
                choice = myCommand()
                os.startfile(files[choice - 1])
            else:
                name = command.replace('open ', '').replace('launch ', '')
                open_apps(name)
                speak('opening...')
                time.sleep(1)
                speak('opened')


    elif 'close' in command:
        name = command.replace("close ", "").strip()
        print(name)
        close_app(name)
        speak("closing")
        time.sleep(1)
        speak("closed")
    elif 'play ' in command:
        if 'song' in command:
            speak('What song shall I play Sir?')
            mysong = myCommand()
            url = player.play_song(mysong)
            speak("")
            speak('you want to watch on youtube or on pc')
            choice = myCommand().lower()
            if url !=None:
                player.play(url,choice)
            else:
                speak("I have not found anything in Youtube")
                pass
        elif 'video' in command:
            speak('Which video shall I play Sir?')
            myvedio = myCommand()
            open_url = "https://www.youtube.com/results?search_query=" + myvedio
            webbrowser.open(open_url)
            url_list = player.play_video(myvedio)
            if url_list!=None:
                speak("Out of five vedios which you want to play ")
                choice=myCommand()
                if choice in choice_list:
                    choice = choice_dict[choice]
                else:
                    choice = choice
                url = url_list[choice - 1]
                speak('you want to watch on youtube or on pc')
                choice1 = myCommand().lower()
                if url != None:
                    player.play(url,choice1)
            else:
                speak("I have not found anything in Youtube")
                pass

    elif "google" in command:
        os.startfile("www.google.com")
    elif "download" in command:
        if 'movie' in command:
            speak('which movie sir')
            movie_name = myCommand()
            try:
                movie_name1, movie_url = movie_downloader.down_movie(movie_name)
            except:
                movie_name1=[]
                speak("i have not found that movie sir")
                pass
            if len(movie_name1) >= 1:
                lenght_list=len(movie_name1)
                speak("i found %d movies"%lenght_list)
                for movie in movie_name1:
                    print(movie_name1)
                choice = myCommand()
                if 'tell' in choice:
                    for i in range(len(movie_name)):
                        speak(movie_name[i])
                else:
                    if choice in choice_list:
                        choice = choice_dict[choice]
                    else:
                        choice = choice
                try:
                    os.startfile(movie_url[choice - 1])
                except:
                    pass
        elif 'game' in command:
            speak('which game sir')
            game_name = myCommand()
            game_name1, game_url = game_downloader.game_name(game_name)
            if len(game_name1) < 1:
                speak("i have not found that game sir")
                pass

            try:
                if len(game_name1) >= 1:
                    num = len(game_name1)
                    speak("i found %d games"%num)
                    for game in game_name1:
                        print(game_name1)
                    choice = myCommand()
                    if choice in choice_list:
                        choice = choice_dict[choice]
                    else:
                        choice = choice
                    try:
                        os.startfile(game_url[choice - 1])
                    except:
                        pass
            except:
                pass

    elif 'send' in command:
        speak('On facebook')
        command=myCommand().lower()
        if "facebook" in command or command=='yes':
            data=fb.account()
            try:
                data=data['username']
            except:
                data=None
            if data != None:
                speak("to whome sir")
                name = myCommand()
                speak("what's the message sir")
                msg = myCommand()
                sent = fb.message(name, msg)
                speak(sent)
            else:
                speak("you have not login with facebook")
        elif "sms" in command:
            with open('JSON_FILE\\info.json') as f:
                data = json.load(f)
            speak('to whom sir')
            command=myCommand()
            try:
                for info in data['info']:
                    phone_num = info[command]
                    speak("what's the message")
                msg = myCommand()
                sendsms.sms(phone_num, msg)
                speak("message sent successfully")
            except:
                speak("number not found")
    elif "enable"in command and "keyboard" in command:
        os.startfile("c:\\User\\abhis\\PycharmPoject\\voiceass\\venv\\keyboard_controle.py")




    elif 'time' in command:
        now = datetime.datetime.now()
        speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

    elif 'current weather' in command:
        weather_info(command)
        
    elif 'lock' in command:
        speak('Sure sir')
        for value in ['pc', 'system', 'windows']:
            ctypes.windll.user32.LockWorkStation()

    elif 'joke' in command:
        res = requests.get(
            'https://icanhazdadjoke.com/',
            headers={"Accept": "application/json"})
        if res.status_code == requests.codes.ok:
            speak(str(res.json()['joke']))
        else:
            speak('oops!I ran out of jokes')


    elif 'shutdown' in command:
        speak('Bye bye Sir. Have a nice day')
        os.system("shutdown -s -t 2")
    elif 'restart' in command:
        speak('you Pc is restarting')
        os.system("shutdown /r -t 2")
    else:
        return None
