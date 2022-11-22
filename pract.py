#Notice: Program cannot run without internet connection


import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import numpy
import pyautogui
import requests
import pywhatkit as kit
import smtplib
#from decouple import config
import os
import time

import requests
#from functions.online_ops import find_my_ip, get_latest_news, get_random_joke, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
#from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from pprint import pprint


# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)  # 1 for female and 0 for male voice
engine.setProperty('rate', 190) #voice speed
engine.setProperty('volume', 1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I don't understand. Can you please repeat that?")
        return "None"
    return query

def search_google(query):
    kit.search(query)

def send_whatsapp_message(whaNum, whaMssg):
    kit.sendwhatmsg_instantly(f"+232{number}", message)


if __name__ == '__main__':

    speak("Adrit assistance activated. ")
    time.sleep(1)
    speak("Hello, Mr Dominic")

    NEWS_API_KEY = config("NEWS_API_KEY")
    OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
    TMDB_API_KEY = config("TMDB_API_KEY")
    EMAIL = config("EMAIL")
    PASSWORD = config("PASSWORD")

    #speak("What to do?")



##########################################################################taking in queries from the user and statically processing it######################################################################################################


    
    while True:
        query = take_command().lower()
        if 'Adrit' in query:
            speak("Who summons me?")
            print("Who summons me?")
        elif 'who are you' in query:
            speak("I am Adrit, developed by Dominic OT")
            print("Adrit")
        elif 'what are you' in query:
            speak("I am an Artificial Intelligence designed to assist you.")
        elif 'what can you do' in query:
            speak("I can take in and process your commands.")
            speak("I will soon be able to expand my library on my own, very soon.")
        elif 'how old are you' in query:
            speak("I am only a few days old.")
        elif 'where are you from' in query:
            speak("I'm from CodeVerse. Have you been there?")




##########################################################################online queries##########################################################################
        #taking random wikipedia apprs
        elif 'open wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
                
        
        #google
        elif 'search google' in query:
            speak("What do you want me to search on Google, sir?")
            query = take_command().lower()
            search_google(query)

        #whatsapp
        elif 'send WhatsApp message' in query:
            speak("What number shall I send the message to, sir?")
            speak("Please type in sir.")
            whaNum = int(input("enter whatsapp number: "))
            time.sleep(1)
            speak("What is the message, sir?")
            whaMssg = take_command().lower()
            send_whatsapp_message(whaNum, whaMssg)
            speak("Message sent sir. What else can I do for you Mr Dominic?")



        elif 'Emmanuel'in query:
            speak("Future Mr. Unimak.")
        elif 'what is my name' in query:
            speak("If I can read your voice well, your name is Dominic OT. You are a genius.")
        elif 'what are you' in query:
            speak("I am Adrit developed by Dominic OT")

#
        elif 'eat for breakfast' in query:
            speak("Options for breakfast:... ")
            speak("Bread & tea, ..., white rice and tomato stew, ..., noodles and boiled EGG.")
        
            
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://www.github.com/dominicOT")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("https://www.spotify.com")
        elif 'hydrate' in query:
            speak("searching for 'hydrate'")
            webbrowser.open("https://www.google.com/hydrate")
        elif 'activate' in query:
            speak("I am already activated.")




###################################local drive#######################################


        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        
        elif query == 'nothing':
            speak("Okay sir.")
        elif 'sleep' in query:
            exit(0)
