import speech_recognition as sr   #(#The as keyword is used to give a shorter or alias name to the module when importing it. This is especially helpful if the module name is long or if you want to avoid name conflicts.)
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi = "enter your api"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

# Initialize the mixer module
    pygame.mixer.init()

# Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play the audio
    pygame.mixer.music.play()
    while pygame.mixer.music.play():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")




def aiprocess(command):
    client=OpenAI(
    api_key="enter your api "
    )     
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant namaed jarvis skilled in general tasks like google cloud and alexa . Give shorter responses please  "},
            {"role": "user","content": command}
            ]
            )
    return (completion.choices[0].message.content)


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]

        link = musicLibrary.music[song]
        webbrowser.open(link) 
    elif "news" in  c.lower():
        r=requests.get(f" https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code==200:
            data=r.json()
            articles=data.get('articles',[])
            for article in articles :
                speak(article['titles'])
    else:
        output=aiprocess(c)
        speak(output)
      

    
 
if __name__ == "__main__":
    speak("initialzing jarvis...")
    while True:
        r=sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower())=="jarvis":
                speak("ya")
                with sr.Microphone() as source:
                    print("jarvis active...") 
                    print("listening..")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)


        except Exception as e:
            print("error;{0}".format(e))