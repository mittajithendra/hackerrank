import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import time

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, sir!!")
    elif hour>=12 and hour<=17:
        speak("Good Afternoon, sir!!")
    else:
        speak("Good Night Sir")
    speak("Hello I am jarvis , How can I help You,sir")

def takeCommand():
    r=sr.Recognizer()
    microphone = sr.Microphone()
    with microphone as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("I can't recognize say that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mittajithendra46@gmail.com','ammanananenu')
    server.sendmail('mittajithendra46@gmail.com',to,content)
    server.close()
    
    


if __name__ == "__main__":
    #speak("jithendra okay u guy fix")
    wishme()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia",'')
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chromedir="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromedir).open("youtube.com")
        elif 'open google' in query:
            chromedir="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromedir).open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' or 'next song' in query:
            music_dir=r'D:\son'
            songs=os.listdir(music_dir)
            rand=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[rand]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,thetime is {strTime}")
        elif 'open code' in query:
            opencode=""
        elif 'email to henry' in query:
            try:
                speak("What should I send")
                content=takeCommand()
                to='adityavardhan1717@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)

        elif 'wait for sometime' in query:
            time.sleep(2000)
        
                
        
            















        
