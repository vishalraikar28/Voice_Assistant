import speech_recognition as sr #module is used to recognize speech and converts into text
import pyttsx3
import webbrowser
import os
import calendar
import pywhatkit
import ecapture as ec
import tkinter as tk
#method is used to speak

 
def speak(text):
     engine=pyttsx3.init('sapi5')
     voice=engine.getProperty("voices")
     engine.setProperty("voice",voice[1].id)
     engine.say(text)
     engine.runAndWait()
#method is used to take input
#listener=sr.Recognizer()
def Take_Input():
 try:
  listener=sr.Recognizer() #instance of recognizer class
  with sr.Microphone() as source:
       #listener.adjust_for_ambient_noise(source,1.2)
       print("listening..")
       listener.energy_threshold=300
       voice=listener.listen(source,timeout=5,phrase_time_limit=5)
       #print("Recognizing...")    
       text=listener.recognize_google(voice,language='en-in')    #this method converts voice to text
       print(text)  #print voice
       #speak(text) #callig speak method from projecta file
 except:
    print("try again")
    return "NONE"
 return text

if __name__=="__main__" :
 while True:
  text = Take_Input().lower()
  if 'open camera' in text:
      speak("Launching")
      os.startfile("microsoft.windows.camera:")  
  elif 'play' in text or 'song' in text:
        speak("playing")#fun calling
        pywhatkit.playonyt(text)#it plays sotube 
  elif 'shutdown' in text or 'turn off' in text:
      speak("hold on a seccond your system is on its way to shutdown")
      speak("make sure all of your application are closed")
      os.system("shutdown /s")
  elif 'restart' in text:     
      speak("hold on a seccond your system is on its way to shutdown")
      speak("make sure all of your application are closed")
      os.system("shutdown /r")
  elif 'sleep' in text:
      os.system("shutdown /h")
  elif 'open calendar' in text:
   try:
    speak("which year calendar you want to display")
    user_input=Take_Input()
    print(calendar.calendar(int(user_input))) 
   except:
    print("didn't recognize your voice")
  elif 'wps' in text:
      os.startfile(r"C:\Users\veeresh\Desktop\WPS Office.lnk")
  elif 'file manager'in text:
      os.system("start..")    
  elif 'exit'in text:
      exit()
  elif 'search' in text: 
   search="https://www.google.com/search?q="+text
   webbrowser.open(search)
  elif 'open' in text:
     from sub_project import *
     openappweb(text)
  elif 'close' in text:
     from sub_project import *
     closeappweb(text)
#window = tk.Tk()
#window.title("desktop Assistant")
#label = tk.Label(window,text="welcome to desktop assistant")
#label.pack()
#speak_button=tk.Button(window,text="speak",command=)

  
   