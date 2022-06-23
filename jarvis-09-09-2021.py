import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
from playsound import playsound
import pyjokes
import subprocess
import winshell
import ctypes
from urllib.request import urlopen
import json
import keyboard
from PyDictionary import PyDictionary as diction
from googletrans import Translator
from bs4 import BeautifulSoup
import requests
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate',185)

def Speak(audio):
    print("   ")  
    engine.say(audio)
    print(f": {audio}")
    print("   ") 
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
     Speak("good morning")

    elif hour>=12 and hour<18:
     Speak("Good Afternoon!")   

    else:
     Speak("Good Evening!")  

    Speak("I am Jarvis Sir,how may I help you?")

def takecommand(): 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except Exception as e:
        print("please say that again")   
        return "None"
        
    return query

def whatsapp():
    Speak("whom do you want to send the message?")
    name = takecommand().lower()

    if 'mum' in name:
     Speak("whats the message?")
     msg = takecommand().lower()
     pywhatkit.sendwhatmsg_instantly("+919010274476",msg)   
     Speak("ok sir, message sent!") 

    elif 'dad' in name:
     Speak("whats the message?")
     msg = takecommand().lower()
     pywhatkit.sendwhatmsg_instantly("+919848029176",msg)   
     Speak("ok sir, message sent!") 

def dict():
   Speak("dictionary activated")
   Speak("what should I search for?")
   probl= takecommand().lower()

   if 'meaning' in probl:
       probl = probl.replace("what is the","")
       probl = probl.replace("jarvis","")
       probl = probl.replace("meaning of","")
       result = diction.meaning(probl)
       Speak(f"the meaning for {probl} is {result} ")

   elif 'synonym' in probl:
       probl = probl.replace("what is the","")
       probl = probl.replace("jarvis","")
       probl = probl.replace("synonym of","")
       result = diction.synonym(probl)
       Speak(f"the synonym for {probl} is {result} ") 

   elif 'antonym' in probl:
       probl = probl.replace("what is the","")
       probl = probl.replace("jarvis","")
       probl = probl.replace("antonym of","")
       result = diction.antonym(probl)
       Speak(f"the antonym for {probl} is {result} ")       

def speedTest():
    import speedtest
    Speak("checking speed...")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    query = takecommand().lower()

    if 'upload' in query:
        Speak(f"the uploading speed is {correctUpload} mbps")

    elif 'download' in query:
        Speak(f"the downloading speed is {correctDown} mbps")

    else:
        Speak(f"the uploading speed is {correctUpload} mbps and the downloading speed is {correctDown} mbps")

def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

def Tran():
   Speak("Tell Me The Line!")
   line = TakeHindi()
   traslate = Translator()
   result = traslate.translate(line)
   Text = result.text
   Speak(Text)

def weather():
        search = "weather in my location"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"The weather Outside Is {temperature}")

        Speak("is there any other place you want to search?")
        next = takecommand().lower()

        if 'yes' in next:
            Speak("Tell Me The Name Of tHE Place ")
            name = takecommand().lower()
            search = f"weather in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {name} is {temperature}")

        else:
            Speak("no problem sir")

if __name__ == "__main__":
    wishMe()
    while True:

      query = takecommand().lower()

      if 'music' in query:
        Speak("Tell Me The NamE oF The Song!")
        musicName = takecommand()
        pywhatkit.playonyt(musicName)
        Speak("Your Song is playing , Enjoy Sir!")

      elif 'open code' in query:
       Speak("Ok Sir , Wait A Second!")
       os.startfile("C:\\Users\\GANESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
       Speak("opened sir!")

      elif 'open browser' in query:
       Speak("Ok Sir , Wait A Second!")
       os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")
       Speak("opened sir!")
        
      elif 'open facebook' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.facebook.com/')
       Speak("opened sir!")

      elif 'open instagram' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.instagram.com/')
       Speak("opened sir!")

      elif 'open maps' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.google.co.in/maps/@17.4383478,78.4638268,15z?hl=en')
       Speak("opened sir!")

      elif 'open youtube' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.youtube.com')
       Speak("opened sir!")

      elif 'open prime' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.primevideo.com/')
       Speak("opened sir!") 

      elif 'open hotstar' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.hotstar.com/in')
       Speak("opened sir!") 

      elif 'open Sony LIV' in query:
       Speak("Ok Sir , Wait A Second!")
       webbrowser.open('https://www.sonyliv.com/')
       Speak("opened sir!")  

      elif 'close browser' in query:
       Speak("closing sir...")     
       os.system("TASKKILL /f /im brave.exe")
       Speak("closed sir!")

      elif 'close code' in query:
       Speak("closing sir...")
       os.system("TASKKILL /F /im code.exe")
       Speak("closing sir...")

      if 'hello' in query or 'hey' in query or 'hi' in query:
       Speak("Hello Sir , I Am Jarvis .")
       Speak("Your Personal AI Assistant!")
       Speak("How can I Help You?")

      elif 'how are you' in query:
       Speak("I Am Fine Sir!")
       Speak("What About YOU?")

      elif 'fine' in query or "good" in query:
       Speak("It's good to know that your fine")

      elif 'you need a break' in query or 'bye' in query or 'exit' in query or 'stop' in query :
       Speak("Ok Sir , You Can Call Me Anytime !")
       Speak("Just Say Wake Up Jarvis!")
       exit()
         
      elif 'youtube search' in query:
       Speak("OK sIR , This Is What I found For Your Search!")
       query = query.replace("jarvis","")
       query = query.replace("youtube search","")
       web = 'https://www.youtube.com/results?search_query=' + query
       webbrowser.open(web)
       Speak("Done Sir!")   

      elif 'website' in query:
       Speak("Ok Sir , Launching.....")
       query = query.replace("jarvis","")
       query = query.replace("website","")
       query = query.replace(" ","")
       web1 = query.replace("open","")
       web2 = 'https://www.' + web1 + '.com'
       webbrowser.open(web2)
       Speak("Launched!")

      elif 'wikipedia' in query:
       Speak("Searching Wikipedia.....")
       query = query.replace("jarvis","")
       query = query.replace("wikipedia","")
       wiki = wikipedia.summary(query, sentences = 2)
       Speak(f"According To Wikipedia : {wiki}")

      elif 'joke' in query:
       get = pyjokes.get_joke()
       Speak(get)

      elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break
     
      elif 'remember that' in query:
       remeberMsg = query.replace("remember that","")
       remeberMsg = remeberMsg.replace("jarvis","")
       Speak("You Tell Me To Remind You That :"+remeberMsg)
       remeber = open('data.txt','w')
       remeber.write(remeberMsg)
       remeber.close()

      elif 'what do you remember?' in query:
       remeber = open('data.txt','r')
       Speak("You Tell Me That" + remeber.read()) 

      elif "what's your name?" in query or "What is your name?" in query:
       Speak("My friends call me")
       assname =("Jarvis 1 point o")
       Speak(assname)
       print("My friends call me", assname)

      elif "who made you?" in query or "who created you?" in query:
       Speak("I have been created by vignesh.")

      elif "who are you?" in query:
       Speak("I am your virtual assistant created by vignesh")
 
      elif 'reason for you?' in query:
       Speak("I was created as a Minor project by Mister vignesh")              

      elif "who am i?" in query:
       Speak("If you talk then definitely your human.")
 
      elif "why did you come to this world" in query:
       Speak("Thanks to vignesh. further It's a secret")

      elif "will you be my gf" in query or "will you be my bf" in query:  
       Speak("I'm not sure about, may be you should give me some time")
 
      elif "i love you" in query:
       Speak("It's hard to understand") 

      elif 'lock system' in query:
       Speak("locking the device")
       ctypes.windll.user32.LockWorkStation()
 
      elif 'shutdown system' in query:
       Speak("Hold On a Sec ! Your system is on its way to shut down")
       subprocess.call('shutdown / p /f')
                 
      elif "restart system" in query:
            subprocess.call(["shutdown", "/r"])
             
      elif "hibernate" in query or "sleep" in query:
            Speak("Hibernating")
            subprocess.call("shutdown / h")
 
      elif "log off" in query or "sign out" in query:
            Speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

      elif 'empty recycle bin' in query:
       winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
       Speak("Recycle Bin emptied")
 
      elif "don't listen" in query or "stop listening" in query:
       Speak("for how much time you want to stop jarvis from listening commands")
       a = int(takecommand())
       time.sleep(a)
       print(a)      

      elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/everything?q=apple&from=2021-08-16&to=2021-08-16&sortBy=popularity&apiKey=4b19da04524741cdbf17fefaf8d38737''')
                data = json.load(jsonObj)
                i = 1
                 
                Speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    Speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

      elif 'pause' in query:
         keyboard.press('space bar')    

      elif 'mute' in query:
         keyboard.press('m')

      elif 'skip' in query:
         keyboard.press('l')

      elif 'back' in query:
         keyboard.press('j')

      elif 'full screen' in query:
         keyboard.press('f')

      elif 'film mode' in query:
         keyboard.press('t')
 
      elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')

      elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

      elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

      elif 'history' in query:
         keyboard.press_and_release('ctrl +h')

      elif 'screenshot' in query:
       Screenshot = pyautogui.screenshot()
       Screenshot.save(r'C:\Users\GANESH\Pictures\Screenshots\screenshot.png') 
       Speak("screenshot taken")

      elif 'whatsapp' in query:
          whatsapp()

      elif 'dictionary' in query:
          dict()    

      elif 'translator' in query:
          Tran()

      elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Data Available!")    

      elif "what's the weather" in query or "what's the temperature" in query:
         weather() 

      elif 'internet speed' in query:
          speedTest()   
      
      elif 'download speed' in query:
          speedTest()

      elif 'upload speed' in query:
          speedTest()   

      elif 'how to' in query:
         Speak("getting data from the internet!")
         op = query.replace("jarvis","")
         max_result = 1 
         how_to_func = search_wikihow(op,max_result)
         assert len(how_to_func) == 1
         how_to_func[0].print()
         Speak(how_to_func[0].summary)