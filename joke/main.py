import pyjokes
import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

joke = pyjokes.get_joke()
print(joke)
speak(joke)