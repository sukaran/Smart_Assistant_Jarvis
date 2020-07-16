import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio= r.listen(source)
         
    try:
        print("Recognising")
        query = r.recognize_google(audio,language='en-in')
        print(f"user siad: {query}\n")
        return query
    except Exception as e:
        print(e)
        print("say that again please!")
        return "None"

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email', 'pass')
    server.sendmail('your-email', to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good  Morning")
    elif hour >=12 and hour<18:
        speak("Good  Afternoon")
    elif hour >=18 and hour<24:
        speak("Good  Evening ")
    speak("Hello and welcome to Jarvis, suku baby's personal assistant. I am ready for your commands!!")

if __name__ == "__main__":
    wishMe()
    while True:
        query = command().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\sgsox\\Music\\Music Maker Jam Recordings'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is : {strTime}")
        elif 'open code' in query:
            codepath = 'C:\\Users\\sgsox\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\Programs\\Visual Studio Code\\code.exe'
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath = '"C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"'
            os.startfile(codepath)

        elif 'email' in query:
            try:
                #speak('What')
                to = 'your-email'
                speak("Just speak whatever you want toi send!!")
                content = command()
                sendMail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry email could not be sent!!")

        elif 'quit' in query:
            exit()
