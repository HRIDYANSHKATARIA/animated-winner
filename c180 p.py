from tkinter import *
import speech_recognition as sr 
import pyttsx3
from datetime import datetime 

root = Tk()

root.title("SPEECH TO TEXT")
root.geometry("400x400")


text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("my name is Jarvis")
        print("MY NAME IS JARVIS")
    if "time" in voice_data:
        speak("current time is ")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)


def r_audio():
    speak("how can i help you")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data = ''
        try:
            voice_data = speech_recognisor.recognize_google(audio,language='en-in')
        except sr.UnknownValueError:
            print("PLEASE REPEAT I DID NOT GET THAT")
            speak("please repeat i did not get that")
    respond(voice_data)




r_audio()

src_lang.set('english')

label = Label(root,text="Main language")
label.place(relx=0.01,rely=0.3,anchor=W)

input_label = Entry()
input_label.place(relx=0.02,rely=0.3,anchor=W)

label2 = Label(root,text="Translated language")
label2.place(relx=0.01,rely=0.3,anchor=E)

input_text = Text_Area()
input_text.place(relx=0.02,rely=0.6,anchor=W)

input_label = Entry()
input_label.place(relx=0.08,rely=0.3,anchor=E)

input_text2 = Text_Area()
input_text2.place(relx=0.08,rely=0.6,anchor=E)

btn = Button(root,text="Translate",command=translate)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)





root.mainloop()