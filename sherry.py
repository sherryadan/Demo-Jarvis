from httpx import get
import pyttsx3
import speech_recognition as sr
import datetime
import os 
import cv2
import wikipedia
import webbrowser
import pywhatkit

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# A text to speech function
def speak(audio):   
    engine.say(audio)
    engine.runAndWait()
    print (audio)

# A Speech to Text Function 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing you......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=2 , phrase_time_limit=5)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google_cloud(audio, language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        speak("Say that Again, Please")
        return "none"
    return query

# Wish Function for greetings 
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0  and hour<=12:
        speak("Good Morning Adan")
    elif hour>=12 and hour<=18:
        speak("Good After Noon Adan")
    else:
        speak("Good Night Adan")
    speak("I am Sherry for your Service, How Can I help you Sir ")

if __name__ == "__main__":
    wish()
    # takecommand()
    # speak("This is just a start, I am Jarvis, How are you Adan")

    # while True:
    if 1:
        query = takecommand().lower()

        # Logic building for Adan's Assistant

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "play music" in query:
            npath = "C:\\Users\\Muhammad Adan\\AppData\\Local\\Microsoft\\WindowsApps\\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\spotify.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "get ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your Ip address is {ip}")
        elif "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sectences=2)
            speak("According to wiki pedia {results}")
            print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open w3schools" in query:
            webbrowser.open("www.w3schools.com")
        elif "search google" in query:
            speak("What should I search on google Sir")
            cm= takecommand().lower()
            webbrowser.open("f{cm}") 
        elif "send whatsapp message" in query:
            speak("Whom should I text Sir")
            number= takecommand().lower()
            speak("What should I text Sir")
            message = takecommand().lower()
            pywhatkit.sendwhatmsg("{number}", {message}, 2,26) 
        
        elif "play a song on youtube" in query:
            speak("What should I play Sir")
            cm= takecommand().lower()
            pywhatkit.playonyt("f{cm}") 


        