from __future__ import unicode_literals
import youtube_dl
get_data = ""
serch_keyword = ""
def From_Arabic_To_Franco(letters=""):

    letters = letters.replace("ا", "a")
    letters = letters.replace("ة", "a")
    letters = letters.replace("ب", "b")
    letters = letters.replace("ث", "c")
    letters = letters.replace("د", "d")
    letters = letters.replace("إ", "e")
    letters = letters.replace("ال", "e")
    letters = letters.replace("ف", "f")
    letters = letters.replace("ج", "g")
    letters = letters.replace("ه", "h")
    letters = letters.replace("ك", "k")
    letters = letters.replace("ل", "l")
    letters = letters.replace("م", "m")
    letters = letters.replace("ن", "n")
    letters = letters.replace("ض", "d")
    letters = letters.replace("ص", "s")
    letters = letters.replace("و", "o")
    letters = letters.replace("ق", "q")
    letters = letters.replace("ر", "r")
    letters = letters.replace("س", "s")
    letters = letters.replace("ت", "t")
    letters = letters.replace("ى", "y")
    letters = letters.replace("ف", "v")
    letters = letters.replace("وا", "w")
    letters = letters.replace("غ", "gh")
    letters = letters.replace("ي", "y")
    letters = letters.replace("ظ", "z")

    letters = letters.replace("أ", "2")
    letters = letters.replace("ع", "3")
    letters = letters.replace("خ", "5")
    letters = letters.replace("ط", "6")
    letters = letters.replace("ح", "7")

    letters = letters.replace("ش", "sh")

    letters = letters.replace("ز", "az")


    letters = letters.replace("ابيوسف", "abyusif")

    global get_data
    get_data = letters
    print(letters)
def Change_Word(text=""):
    text = text.replace("abyosf", "abyusif")
    text = text.replace("abo_yosf", "abyusif")
    text = text.replace("3rd_snk", "Arsenik")
    text = text.replace("arsynyk", "Arsenik")
    text = text.replace("arsynk", "Arsenik")
    text = text.replace("arslk", "Arsenik")
    text = text.replace("bs_toth", "batistuta")
    text = text.replace("batystota", "batistuta")
    text = text.replace("bs_tota", "batistuta")
    text = text.replace("ly_gysy", "Lege-Cy")
    text = text.replace("lk_asy", "Lege-Cy")
    text = text.replace("lygasy", "Lege-Cy")
    text = text.replace("mroan_bablo", "MARWAN_PABLO")
    text = text.replace("dyazy_to_skyny", "DIZZYTOOSKINNY")
    text = text.replace("dy_syto_skyny", "DIZZYTOOSKINNY")
    text = text.replace("dy_fy_toskanyny", "DIZZYTOOSKINNY")
    text = text.replace("dy_fy_to_skyny", "DIZZYTOOSKINNY")
    text = text.replace("dy_fy_tmskyny", "DIZZYTOOSKINNY")
    text = text.replace("dy_to_skyny", "DIZZYTOOSKINNY")
    global serch_keyword
    serch_keyword = text
    print()
def Download(url=""):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])