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
sp = "en"
index = 0


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
                search_keyword = test
                print(search_keyword)
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                link = "https://www.youtube.com/watch?v=" + video_ids[0]
                video = pafy.new(link)
                best = video.getbestaudio()
                play_url = best.url
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
                translate.Download(link)
            elif test == "Arabic":
                sp = "ar"
                print("SERVER ---> LANGUAGE CHANGE")
                print("SERVER(LANGUAGE) ---> ARABIC")
                print("SERVER --->مرحبا<--- SERVER")
                speak("مرحبا انت الان تستخدم لغة العربية")
                lan = "ar-EG"
        else:
            print("مرحبا انت الان تستخدم لغة العربية")

            if test.__contains__("افتح"):
                test = re.sub(r'^.*?افتح', 'افتح', test)
                print(index)
                if index >= 1:
                    print("SERVER ---> STOP SONG")
                    player.stop()
                test = test.replace("افتح ", "")
                test = test.replace(" ", "_")
                translate.From_Arabic_To_Franco(letters=test)
                search_keyword = translate.get_data
                translate.Change_Word(text=search_keyword)
                search_keyword = translate.serch_keyword
                print(f"search_keyword = {search_keyword}")
                html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                link = "https://www.youtube.com/watch?v=" + video_ids[0]
                video = pafy.new(link)
                best = video.getbestaudio()
                play_url = best.url
                Instance = vlc.Instance()
                player = Instance.media_player_new()
                Media = Instance.media_new(play_url)
                Media.get_mrl()
                player.set_media(Media)
                player.play()
                index = index + 1
                sw = 0
                print(sw)
                # root = Tk()
                # Label(root, text=f'SERVER ---> YOUR SONG NAME:{search_keyword}', font=("Helvetica 20 bold")).pack()
                # root.after(2000, lambda: root.destroy())
                # root.call('wm', 'attributes', '.', '-topmost', '1')
                # root.mainloop()
                print("SERVER ---> YOUR SONG IS START")
            elif test == "اقفل":
                print("SERVER ---> EXIT")
                player.stop()
            elif test == "وقف":
                print("SERVER ---> PAUSE")
                player.pause()
                sw = 1
                print(sw)
            elif test == "شغل":
                print("SERVER ---> RESUME")
                player.play()
                sw = 0
                print(sw)
            elif test == "اعاده":
                print("SERVER ---> REPEAT")
                player.stop()
                player.play()
            elif test == "تحميل":
                translate.Download(link)
            elif test == "انجليزي":
                sp = "en"
                print("SERVER ---> LANGUAGE CHANGE")
                print("SERVER(LANGUAGE) ---> ENGLISH")
                print("SERVER --->HI BRO<--- SERVER")
                speak("Hello, you are now using ENGLISH")
                lan = "En"
