import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
from datetime import datetime as dt
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess # to run external pyhton files
import keyboard # for keyboard 
import pyautogui # for screenshot

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    

    else:
        speak("Good Evening!")  

    speak("Hii i am Buddy your personal AI assistant.  How can i help you sir ?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('singhniteesh204@gmail.com', "*******")
    server.sendmail('singhniteesh204@gmail.com', to, content)
    server.close()



def download_file():
    subprocess.run(['python', 'E:\\major project\\Download_file\\download_file.py'])




def weather_forecast():
    subprocess.run(['python', 'E:\\major project\\weather\\weather.py'])



def battery_status():
    subprocess.run(['python', 'E:\\major project\\battery notification\\battery_notification.py'])



def change_volume(increase=True):
    key = "volume up" if increase else "volume down"
    keyboard.press_and_release(key)



def generate_QR():
    subprocess.run(['python', 'E:\\major project\\QR Code\\QR_Code.py'])


def take_screenshot(name):
    # my_screenshot = pyautogui.screenshot()
    # my_screenshot.save(f"E:\\major project\\take_screenshot\\screenshot_images\\{name}.jpeg")
    filename = dt.now().strftime("screenshot_%Y-%m-%d_%H-%M-%S.png")
    pyautogui.screenshot().save(filename)
    print(f"Screenshot saved as '{filename}'")




if __name__ == "__main__":
    wishMe()
    # count = 0
    contact_number = {
        "ravikant" : 6392403945,
        "satyam" : 8318576729,
        "rohit" : 8181039155,
        "sanya" :7607252840,
    }

    contact_email = {
        "ravikant" : "sravikant468@gmail.com",
        "satyam" : "sk4423052@gmail.com",
        "rohit" : "rohitthh0305@gmail.com",
        "sanya" : "",
    }
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "exit" in query or "quit" in query:
            speak("Sure sir! as your wish, bai")
            break
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\programming\\project 3\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send mail' in query:
            try:
                speak("To whome ?")
                to = takeCommand().lower()
                print(to)
                speak("What should I say?")
                content = takeCommand()
                # to = "harryyourEmail@gmail.com" 
                to = contact_email[to]
                print(to)   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry due to some technical error, I am not able to send this email")  

        elif "download file" in query:
            download_file()

        elif "weather forecast" in query:
            weather_forecast()

        elif "open" in query:
            l = query.split()
            # print(l)
            l = l[1]
            print(l)
            subprocess.run(l)

        elif "battery status" in query:
            battery_status()
        
        elif "increase volume" in query:
            change_volume()
        
        elif "decrease volume" in query :
            change_volume(False)

        elif "generate" in query:
            generate_QR()

        elif "screenshot" in query:
            # count = count + 1
            take_screenshot(str())

        else:
            print("No query matched")
