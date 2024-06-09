import pyttsx3
import datetime
import time

e = pyttsx3.init()

def speak(audio):
    e.say(audio)
    e.runAndWait()

def date():
    h = datetime.datetime.now().hour
    if h >= 7 and h <= 12:
        speak("good morning, sir")
    elif h >= 13 and h <= 17:
        speak("good afternoon, sir")
    elif h >= 18 and h <= 19:
        speak("good evening, sir")
    else:
        speak("good night, sir")
    y = int(datetime.datetime.now().year)
    m = int(datetime.datetime.now().month)
    d = int(datetime.datetime.now().day)
    speak(f"Today's date is {y}, {m}, {d}")

def get_time():
    t = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(t)

def main():
    speak("Welcome back sir, i'm your ai assistent")
    date()
    get_time()
    speak("i will remind you in 10 second")

while True:
    main()
    time.sleep(10)