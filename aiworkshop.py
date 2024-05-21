import pyttsx3
import speech_recognition as sr
import wikipedia
import pyautogui
x=pyttsx3.init()
import datetime
import json
import requests
import pywhatkit as kit
import smtplib
import musicplayer
import os


headers = {"Authorization": "Paste your EDEN AI API KEY HERE"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Naveen"
}

def call_to_openai(query):
    payload["text"]=query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['generated_text'])
    speak(result['openai']['generated_text'])
# /******************************************************************************/
def speak(audio):
    x.say(audio)
    x.runAndWait()
# /******************************************************************************/
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    speak(t)
# /******************************************************************************/
def date():
    y=str(datetime.datetime.now().year)
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
# /******************************************************************************/
def wish():
    h=datetime.datetime.now().hour
    if(h<12):
        speak("Good Morning")
    elif(h>=12 and h<=18):
        speak("Good Afternoon")
    elif(h>18 and h<=21):
        speak("Good Evening")
    else:
        speak("Good Night")
    speak("Hi This is AI")
    speak("How Can I help You")
# wish()
# /******************************************************************************/
def screenshot():
    im1 = pyautogui.screenshot()
    # im1.save('C:/Users/navee/Desktop/AI/image.png')
    im1.save('myscreenshot1.png')
# /******************************************************************************/
def youtube(elem):
    kit.playonyt(elem)
# /******************************************************************************/
def browse(ques):
    kit.search(ques)
# /******************************************************************************/
def whatsapp(t,msg):
    kit.sendwhatmsg_instantly(t,msg)
# /******************************************************************************/
def sendemail(to,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nbhavanam934@gmail.com','fytk xkvl ycdf wmzl')
    server.sendmail('nbhavanam934@gmail.com',to,msg)
    server.close()
def inp():
    x1=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        x1.pause_threshold=1
        audio=x1.listen(source)
        try:
            print("Recognizing")
            query= x1.recognize_google(audio,language="en-in")
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again please")
            inp()
            return "None"
        return query
# inp()
# /******************************************************************************/
if __name__=="__main__":
    wish()
    while True:
        query=inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            print("Browsing wikipedia.....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
            print(result)
        elif "screenshot" in query:
            print("Your Screenshot is being captured")
            speak("Your Screenshot is being captured")
            screenshot()
        elif "open youtube" in query:
            try:
                speak("What you want to browse ?")
                elem=inp()
                speak("Opening youtube....")
                youtube(elem)
            except Exception as e:
                print(e)
                speak("Failed to open youtube") 
            # exit()
        elif "open chrome" in query:
            try:
                speak("What you want to search ?")
                ques=inp()
                speak("Browsing")
                browse(ques)
            except Exception as e:
                print(e)
                speak("Failed to browse") 
        elif "send in whatsapp" in query:
            try:
                speak("Input Recepient as Text")
                t=input()
                speak("Say MSG to send")
                msg=inp()
                whatsapp(t,msg)
            except Exception as e:
               print(e)
               speak("Failed to send")
        elif "remember" in query:
            speak("What to be remembered ?")
            data=inp()
            speak("Your input is"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "speak out data" in query:
            remember=open('data.txt','r')
            speak("The data I stored is"+remember.read())
            # print("The data I stored is"+)
        elif "send email" in query:
            try:
                speak("What you want to send")
                msg=inp()
                speak("Enter recipient email")
                to=input()
                sendemail(to,msg)
                speak("It's success")
            except Exception as e:
                print(e)
                speak("Failed to send")
        elif "play song" in query:
            song_path=input("Enter a Song path")
            musicplayer.playsong(song_path)
        elif "stop song" in query:
            musicplayer.control("Stop")
        elif "pause song" in query:
            musicplayer.control("Pause")
        elif "resume song" in query:
            musicplayer.control("Resume")
        elif "exit" in query:
            speak("Exiting")
            print("bye bye")
            exit()
        else:
            call_to_openai(query)
