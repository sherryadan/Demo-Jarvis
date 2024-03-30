import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

# A text-to-speech function
def speak(audio):   
    engine.say(audio)
    engine.runAndWait()
    print(audio)

# A function to take user input as voice 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = r.listen(source, timeout=5)  # Listen for 5 seconds
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
        return query

    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
    except sr.RequestError:
        speak("Sorry, I'm unable to access the Google API at the moment. Please try again later.")
    return None

if __name__ == "__main__":
    user_input = takecommand()
    if user_input:
        speak("You said: " + user_input)
