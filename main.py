from __future__ import unicode_literals
import os
import time
import urllib.request
import pafy
import vlc
import playsound
import speech_recognition as sr
from gtts import gTTS
import translate
from tkinter import *
import keyboard

lan = "ar-EG"
sp = "ar"
index = 0
f = open("Donwload_Song.txt",'r+')
flag = 0
lines = 0


def speak(text):
    tts = gTTS(text=text, lang=sp)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=3)
        said = ""

        try:
            said = r.recognize_google(audio, language=lan)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


while True:
    if keyboard.is_pressed("]"):
        test = get_audio()
        time.sleep(0.1)
        print(test)
        time.sleep(0.1)
        if lan == "En":
            print("Hello, you are now using ENGLISH")
            if test.__contains__("open"):
                print(index)

                if index >= 1:
                    print("SERVER ---> STOP SONG")
                    player.stop()
                test = test.replace("open ", "")
                test = test.replace(" ", "_")
                translate.From_Arabic_To_Franco(letters=test)
                search_keyword = translate.get_data
                translate.Change_Word(text=search_keyword)
                search_keyword = translate.serch_keyword
                print(f"search_keyword = {search_keyword}")
                for line in f:
                    index += 1
                    if search_keyword in line:
                        flag = 1
                        break
                if flag == 0:
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    link = "https://www.youtube.com/watch?v=" + video_ids[0]
                    video = pafy.new(link)
                    best = video.getbestaudio()
                    play_url = best.url
                else:
                    play_url = f"{search_keyword} + .mp3"
                    print("SERVER ---> NO_INTERNET")
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(play_url)
                Media.get_mrl()
                player.set_media(Media)
                speak("SERVER ---> (Song Will Start Now)")
                player.play()
            elif test == "Hi Hello":
                player.stop()
            elif test == "exit":
                print("SERVER ---> EXIT")
                player.stop()
            elif test == "stop":
                print("SERVER ---> PAUSE")
                player.pause()
            elif test == "play":
                print("SERVER ---> RESUME")
                player.play()
            elif test == "repeat":
                print("SERVER ---> REPEAT")
                player.stop()
                player.play()
            elif test == "download":
                translate.Download(link, search_keyword)
                f.write(search_keyword + "\n")
                with open('Donwload_Song.txt', 'a') as f:
                    f.writelines(search_keyword + "\n")
                print("SERVER ---> FILE DOWNLOAD")
            elif test == "Arabic":
                sp = "ar"
                print("SERVER ---> LANGUAGE CHANGE")
                print("SERVER(LANGUAGE) ---> ARABIC")
                print("SERVER --->??????????<--- SERVER")
                speak("?????????? ?????? ???????? ???????????? ?????? ??????????????")
                lan = "ar-EG"
        else:
            print("?????????? ?????? ???????? ???????????? ?????? ??????????????")

            if test.__contains__("????????"):
                test = re.sub(r'^.*?????????', '????????', test)
                print(index)
                if index >= 1:
                    print("SERVER ---> STOP SONG")
                    player.stop()
                test = test.replace("???????? ", "")
                test = test.replace(" ", "_")
                translate.From_Arabic_To_Franco(letters=test)
                search_keyword = translate.get_data
                translate.Change_Word(text=search_keyword)
                search_keyword = translate.serch_keyword
                print(f"search_keyword = {search_keyword}")
                for line in f:
                    index += 1
                    if search_keyword in line:
                        flag = 1
                        break
                if flag == 0:
                    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                    link = "https://www.youtube.com/watch?v=" + video_ids[0]
                    video = pafy.new(link)
                    best = video.getbestaudio()
                    play_url = best.url
                else:
                    play_url = f"{search_keyword} + .mp3"
                    print("SERVER ---> NO_INTERNET")
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(play_url)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                index = index + 1
                print("SERVER ---> YOUR SONG IS START")
                speak("???????????? ???????????? ????????????")
            elif test == "????????":
                print("SERVER ---> EXIT")
                player.stop()
            elif test == "??????":
                print("SERVER ---> PAUSE")
                player.pause()
            elif test == "??????":
                print("SERVER ---> RESUME")
                player.play()
            elif test == "??????????":
                print("SERVER ---> REPEAT")
                player.stop()
                player.play()
            elif test == "??????????":
                translate.Download(link,search_keyword)
                f.write(search_keyword + "\n")
                with open('Donwload_Song.txt', 'a') as f:
                    f.writelines(search_keyword + "\n")
                print("SERVER ---> FILE DOWNLOAD")
            elif test == "??????????????":
                sp = "en"
                print("SERVER ---> LANGUAGE CHANGE")
                print("SERVER(LANGUAGE) ---> ENGLISH")
                print("SERVER --->HI BRO<--- SERVER")
                speak("Hello, you are now using ENGLISH")
                lan = "En"