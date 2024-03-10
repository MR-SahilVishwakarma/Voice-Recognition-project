import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import opencage
import folium
import phonenumbers
from phonenumbers import timezone , geocoder , carrier

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    time1 = int(datetime.datetime.now().hour)
    if time1>=0 and time1<12:
        speak("good morning!")
    elif time1>=12 and time1 <18:
        speak('good afternoon!')
    else :
        speak('good evening!')

def takeCommand():
    #for voice input str op
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception :
        print("Bartan again")
        return "None"
    return query
if __name__ == "__main__":
    speak("hello boss")
    wishMe()
    while True:
        def takeCommand():
    #for voice input str op
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)

            try:
                print('Recognising...')
                query = r.recognize_google(audio, language= 'en-in')
                print(f"User said: {query}\n")

            except Exception :
                print("Bartan again")
                return "None"
            return query
        query = takeCommand().lower()
        # for executing task
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query =query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        
        elif 'open assistant code' in query:
            assistantpath='C:\\Users\\Lenovo\\Desktop\\acc proj\\assistent'
            os.startfile(assistantpath)
        elif 'open vs code' in query:
            codepath='"C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)

        elif 'find phone number detail' in query:
            speak("Enter number with +91")
            number = input("Enter number with +91: ")
            phone = phonenumbers.parse(number)
            print(phone)
            time = timezone.time_zones_for_number(phone)
            car = carrier.name_for_number(phone, "en")
            reg = geocoder.description_for_number(phone, "en")
            print(time)
            speak(time)
            print(car)
            speak(car)
            print(reg)
            speak(reg)

            
            from opencage.geocoder import OpenCageGeocode 

            key = 'e431b2c3bd5643faa07dc8b82031bfc6'
            geocoder = OpenCageGeocode(key)
            query = str(reg)
            results = geocoder.geocode(query)
            # print(results)
            lat = results[0]['geometry'] ['lat']
            long = results[0]['geometry'] ['lng'] 
            print (lat, long)

            mymap = folium.Map(location = [lat, long], zoom_start= 9)
            folium.Marker([lat, long], popup= reg).add_to(mymap)

            mymap.save("location.html")
                    

        