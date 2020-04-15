import cx_Freeze
from cx_Freeze import *

if (sys.platform == "win32"):
    base = "Win32GUI"
executables = [cx_Freeze.Executable("jerry.py", base=base)]

setup(
    name = 'jerry',
    options = {'build_exe':{'packages': ['speech_recognition','pyttsx3','time',
                                         'wikipedia','re','google','AI','fb',
                                         'game_downloader','movie_downloader',
                                         'player','sendsms','pynput','keyboard_controle',
                                         'os','fbchat','bs4','urllib',
                                         'datetime','requests','webbrowser',
                                         'youtube_dl','json','fbchat','win32com.server.util',
                                         'pyqt5','psutil','apps_names','search_file','speech_recog',
                                         'taskmanger','web_browser','user_ui','playsound','threading']}},
    executables=executables
    )


"python setup.py bdist_msi"
