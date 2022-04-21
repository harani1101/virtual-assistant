from contextlib import ContextDecorator
from ctypes import c_bool, c_byte
import pyttsx3
import requests 
import speech_recognition as sr 
import webbrowser   
import datetime 
import pyautogui  
import wikipedia    
import random
import os
import json
#import winshell
import pyjokes
import smtplib
import time
import re, requests, subprocess, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pywhatkit as pwt
import wolframalpha as wf
from win10toast import ToastNotifier



def speak(audio):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)



def Date():
    year=int(datetime.datetime.now().year)
    month=datetime.datetime.now().month
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',3: 'Wednesday', 4: 'Thursday',5: 'Friday', 6: 'Saturday',7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def wishme():

    speak("Welcome back Prathyusha!")
    #os.startfile("C:")
    hour=datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good Evening")
    else:
        speak("Good night")

    speak("How may I help you???")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold= 0.5
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en=in')
        print(query)
        #speak(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login("prathyusha.research13@gmail.com", "myresearch")
    server.sendmail("prathyusha.research13@gmail.com",to, content)
    server.close()

    

def jokes():
    result=pyjokes.get_joke()
    print(result)
    speak(result)
    

def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\jarvis ss\ss.png")

def weather():
	city = "Visakhapatnam"
	res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
	temp1 = res["weather"][0]["description"]
	temp2 = res["main"]["temp"]
	print(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
	speak(f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")



def Take_query():

    wishme()

    while(True):
        query=takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            Date()
        elif "quit" in query or "bye" in query or "exit" in query or "stop" in query or "offline" in query:
            exit()
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)


        elif "open google" in query or "google" in query:
            wb.open_new_tab("www.google.com")
            
          


        elif "open gmail" in query:
            speak("Opening Gmail ")
            wb.open_new_tab("www.gmail.com")
            #time.sleep(5)
        elif "headlines" in query:
            speak("Here are some headlines from the Times of India, Happy reading")
            wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        elif "open youtube" in query:
            speak("Opening youtube")
            wb.open("www.youtube.com")
        elif "open whatsapp" in query:
            speak("Opening Whatsapp")
            wb.open("https://web.whatsapp.com/")

        elif "joke" in query:
            jokes()

        elif "screenshot" in query:
            screenshot()
            speak("Done taking the screenshot")

        elif "weather" in query or "climate" in query:
            weather()

        elif "day" in query:
            tellDay()

        
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                print("Enter the email address of the receiver: ")
                to = input()  
                SendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        
        
        elif "show me" in query:
            
            try:
                ind=query.lower().split().index("me")
                location=query.split()[ind + 1:]
                url="https://www.google.com/maps/place/"+"".join(location)
                #speak("This is where"+str(location)+"is")
                wb.open(url)
            except Exception as e:
                print(e)
        
        elif "calculate" in query:
            app_id="YPAGX9-7PJPTPV4TK"
            client= wolframalpha.Client(app_id)
            ind=query.lower().split().index("calculate")
            query=query.split()[ind + 1:]
            res=client.query(" ".join(query))
            answer=next(res.results).text
            speak("the answer is" + answer)
            print("the answer is" + answer)
        
        elif "what is " in query or "who is"  in query:
            app_id="YPAGX9-7PJPTPV4TK"
            client= wolframalpha.Client(app_id)
            ind=query.lower().split().index("is")
            query=query.split()[ind + 1:]
            res=client.query(" ".join(query))
            answer=next(res.results).text
            speak("the answer is " + answer)
            print("the answer is " + answer)

        elif "how many"  in query:
            app_id="YPAGX9-7PJPTPV4TK"
            client= wolframalpha.Client(app_id)
            ind=query.lower().split().index("many")
            query=query.split()[ind + 1:]
            res=client.query(" ".join(query))
            answer=next(res.results).text
            speak("the answer is " + answer)
            print("the answer is " + answer)
        
        elif 'play' in query:
            query = query.replace("play", "")
            query_string = urllib.parse.urlencode({"search_query": query})
            formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
            clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
            print(clip2)         
            wb.open(clip2)
        
        elif 'drive' in query:
            speak("which drive should I open?")
            name=takeCommand()
            os.startfile(name+":")
            
       
if __name__=="__main__":
    Take_query()        
#takeCommand()

