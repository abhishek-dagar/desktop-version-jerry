import speech_recognition as sr
import pyttsx3

import psutil

def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listen...')
        r.pause_threshold = 1
        r.energy_threshold=100
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        # loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command=""
        pass
    return command


def cpu():
    cpu_per=psutil.cpu_percent(interval=None)
    mem_usg=psutil.virtual_memory()[2]
    return cpu_per,mem_usg
